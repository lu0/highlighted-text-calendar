import calendar
import os
import sys
import unittest

import pandas as pd

from highlighted_text_calendar import prettify_date_range

pwd = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

CAL_KWARGS = dict(
    firstweekday=calendar.SUNDAY,
    month_margin_right=2,
    months_per_period=6,
)


class TestDateRangePrettifier(unittest.TestCase):
    """
    Tests if the Date Range Prettifier returns the correct
    representation of the date range as a calendar
    """

    def open_expected_calendar(self, name: str) -> str:
        cal_path = f"{pwd}/mock_prettified_calendars/{name}.txt"
        expected_format = ""
        with open(cal_path, "r") as f:
            expected_format = f.read()
        return expected_format

    def test_format_multiyear_range(self) -> None:
        start = "2022-01-31"
        end = "2024-10-30"
        semimonthly = "SM"
        mock_date_range = pd.date_range(start, end, freq=semimonthly)
        expected = self.open_expected_calendar("multiyear_range")
        result: str = prettify_date_range(mock_date_range, **CAL_KWARGS)
        self.assertEqual(expected.rstrip(), result.rstrip())

    def test_format_multiyear_selected_year(self) -> None:
        start = "2022-01-31"
        end = "2024-10-30"
        semimonthly = "SM"
        mock_date_range = pd.date_range(start, end, freq=semimonthly)
        expected = self.open_expected_calendar("multiyear_selected_year")
        result: str = prettify_date_range(mock_date_range, 2023, **CAL_KWARGS)
        self.assertEqual(expected.rstrip(), result.rstrip())

    def test_format_singleyear_range(self) -> None:
        start = "2022-01-15"
        end = "2022-10-30"
        daily = "D"
        mock_date_range = pd.date_range(start, end, freq=daily)
        expected = self.open_expected_calendar("singleyear_range")
        result: str = prettify_date_range(mock_date_range, **CAL_KWARGS)
        self.assertEqual(expected.rstrip(), result.rstrip())

    def test_format_singleyear_selected_year_not_in_range(self) -> None:
        start = "2022-01-15"
        end = "2022-10-30"
        daily = "D"
        mock_date_range = pd.date_range(start, end, freq=daily)
        expected = self.open_expected_calendar("singleyear_not_in_range")
        result: str = prettify_date_range(mock_date_range, 2023, **CAL_KWARGS)
        self.assertEqual(expected.rstrip(), result.rstrip())

    def test_format_year_different_structure(self) -> None:
        start = "2022-01-01"
        end = "2022-12-31"
        weekdays = "B"
        mock_date_range = pd.date_range(start, end, freq=weekdays)
        expected = self.open_expected_calendar("year_different_structure")
        result: str = prettify_date_range(
            date_range=mock_date_range,
            firstweekday=calendar.MONDAY,
            month_margin_right=2,
            months_per_period=4,
        )
        self.assertEqual(expected.rstrip(), result.rstrip())
