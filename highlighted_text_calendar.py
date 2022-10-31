import calendar
from typing import Any, Dict, Iterable, List, Optional

import pandas as pd
from pandas import DatetimeIndex

MONTH_MARGIN_RIGHT = 3
MONTHS_PER_PERIOD = 4
MAX_MONTH_ROWS = 10
DAY_COL_WIDTH = 2
HIDDEN_DAY_SYMBOL = "╶╴"
NEW_LINE = "\n"
DATE_FORMAT = "%Y-%m-%d"
DATE_SEP = "-"
DAY_OUTSIDE_MONTH = 0
FIRST_WEEKDAY = calendar.MONDAY

MonthRows = List[str]
PeriodCols = Iterable[str]


class HighlightedTextCalendar(calendar.TextCalendar):
    """
    Subclass of TextCalendar that outputs a calendar
    as a plain text, similar to the UNIX program call,
    while allowing highlights to specific dates.

    Args:
        date_range (DatetimeIndex): Dates to highlight
        firstweekday (int): First day of the week (0=Monday, 6=Sunday).
        month_margin_right (int): Number of spaces to place to the right
            of each month before starting the next one.
        months_per_period (int): Number of months to display per row.
    """

    def __init__(
        self,
        date_range: DatetimeIndex = DatetimeIndex([]),
        firstweekday: int = FIRST_WEEKDAY,
        month_margin_right: int = MONTH_MARGIN_RIGHT,
        months_per_period: int = MONTHS_PER_PERIOD,
    ) -> None:
        super().__init__(firstweekday)
        self._dates: Dict = self._datetimeindex_to_dict(date_range)
        self._year: Optional[int] = None
        self._month: Optional[int] = None
        self.firstweekday = firstweekday
        self.month_margin_right = month_margin_right
        self.months_per_period = months_per_period

    @staticmethod
    def _datetimeindex_to_dict(date_range: DatetimeIndex) -> Dict:
        """Converts a DatetimeIndex object to a dictionary
        with structure `{year: month: [days]}`"""
        date_range = date_range.sort_values(ascending=True)
        dictified_range: Dict = dict()
        dates: List[str] = list(date_range.strftime(DATE_FORMAT))
        for date in dates:
            year, month, day = [int(s) for s in date.split(DATE_SEP)]
            if year not in dictified_range:
                empty_year: Dict = {i: list() for i in range(1, 13)}
                dictified_range[year] = empty_year
            dictified_range[year][month].append(day)
        return dictified_range

    def _days_to_highlight(self) -> List[int]:
        if self._dates:
            return self._dates.get(self._year, {}).get(self._month, [])
        return []

    def formatday(self, day: int, weekday: int, width: int) -> str:
        """
        Overrides parent function to hide the dates
        outside the range specified during the instantiation
        of the class, using a custom symbol.
        """
        if day != DAY_OUTSIDE_MONTH and day not in self._days_to_highlight():
            return HIDDEN_DAY_SYMBOL
        return super().formatday(day, weekday, width=DAY_COL_WIDTH)

    def _format_as_periods(self, padded_months: List[MonthRows]) -> List[str]:
        periods: List[str] = []
        for start in range(0, 12, self.months_per_period):
            stop: int = start + self.months_per_period
            period_months = padded_months[start:stop]
            if not len(period_months):
                break
            period_matrix: List[PeriodCols] = list(zip(*period_months))
            rows: List[str] = ["".join(col) for col in period_matrix]
            formatted_period = NEW_LINE.join([r for r in rows if r.strip()])
            periods.append(formatted_period)
        return periods

    def _pad_month(self, month: str) -> List:
        rows: List[str] = month.split(sep=NEW_LINE)
        week_header: str = self.formatweekheader()
        y_padded_month: List[str] = rows + [""] * (MAX_MONTH_ROWS - len(rows))
        month_width: int = len(week_header) + self.month_margin_right
        padded_month = [r.ljust(month_width, " ") for r in y_padded_month]
        return padded_month

    def _pad_and_join_as_periods(self, months: List[str]) -> str:
        padded_months: List[MonthRows] = [self._pad_month(m) for m in months]
        formatted_periods: List[str] = self._format_as_periods(padded_months)
        period_sep: str = NEW_LINE * 2
        year_as_periods: str = period_sep.join(formatted_periods)
        return year_as_periods

    def formatmonth(
        self, theyear: int, themonth: int, *args: Any, **kwargs: Any
    ) -> str:
        """
        Overrides parent function in order to store the current month,
        which is then used by `formatday` inside `formatmonth`
        """
        self._month = themonth
        return super().formatmonth(theyear, themonth)

    def _get_formatted_months(self, year: int) -> List[str]:
        return [self.formatmonth(year, m) for m in range(1, 13)]

    def formatyear(self, theyear: int, *args: Any, **kwargs: Any) -> str:
        """
        Overrides parent function to format `theyear` by assembling it
        from individually padded months in order to force calls to
        `formatmonth` and `formatday`, rather than creating a simple
        calendar with no data state and no highlights.
        """
        self._days_to_highlight()
        self._year = theyear
        formatted_months = self._get_formatted_months(theyear)
        formatted_year = self._pad_and_join_as_periods(formatted_months)
        return formatted_year

    def formatweekheader(self, *args: Any, **kwargs: Any) -> str:
        """Overrides parent function to force widht of headers"""
        return super().formatweekheader(width=DAY_COL_WIDTH)

    def format(self) -> str:
        """
        Additional function that generates a complete set of
        highlighted text calendars from all dates contained in
        the range specified during the instantiation of the class.
        """
        week_header: str = self.formatweekheader()
        month_width: int = len(week_header) + self.month_margin_right
        period_width: int = month_width * self.months_per_period
        year_sep: str = NEW_LINE * 2 + "-" * period_width + NEW_LINE * 2
        return year_sep.join([self.formatyear(y) for y in self._dates])


def prettify_date_range(
    date_range: DatetimeIndex,
    year: Optional[int] = None,
    firstweekday: int = FIRST_WEEKDAY,
    month_margin_right: int = MONTH_MARGIN_RIGHT,
    months_per_period: int = MONTHS_PER_PERIOD,
) -> str:
    """Helper function to create text Calendars from a date_range.

    Args:
        date_range (DatetimeIndex): Dates to prettify
        year (optional, int): year to select from the date range.

    Returns:
        (str): A text representation of multiple highlighted calendars
            if `date_range` contains dates across multiple years,
            or a text representation of a single highlighted calendar
            if `date_range` contains dates of a same year or if `year`
            is provided.
            Dates in `date_range` will get highlighted, while other
            will be hidden from the calendar.
    """
    cal = HighlightedTextCalendar(
        date_range=date_range,
        firstweekday=firstweekday,
        month_margin_right=month_margin_right,
        months_per_period=months_per_period,
    )
    if year:
        return cal.formatyear(year)
    return cal.format()

if __name__ == "__main__":
    start = "2022-01-31"
    end = "2024-10-30"
    semimonthly = "SM"
    date_range = pd.date_range(start, end, freq=semimonthly)
    pretty_calendar: str = prettify_date_range(date_range)
    print(pretty_calendar)
