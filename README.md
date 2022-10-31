# Highlighted Python Text Calendar

Subclass of TextCalendar that allows highlighting dates specified in a DatetimeIndex


TODO: Make it terminal/ansible printable (highlight rather than hiding other dates)

## Usage

```sh
python3 highlighted_text_calendar.py
```

```txt
    January 2022          February 2022            March 2022             April 2022        
Mo Tu We Th Fr Sa Su   Mo Tu We Th Fr Sa Su   Mo Tu We Th Fr Sa Su   Mo Tu We Th Fr Sa Su   
               ╶╴ ╶╴      ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴      ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴               ╶╴ ╶╴ ╶╴   
╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   
╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ 15 ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ 15 ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ 15 ╶╴ ╶╴   
╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   
╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   28                     ╶╴ ╶╴ ╶╴ 31            ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ 30      
31                                                                                          

      May 2022              June 2022              July 2022             August 2022        
Mo Tu We Th Fr Sa Su   Mo Tu We Th Fr Sa Su   Mo Tu We Th Fr Sa Su   Mo Tu We Th Fr Sa Su   
                  ╶╴         ╶╴ ╶╴ ╶╴ ╶╴ ╶╴               ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   
╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   
╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ 15   ╶╴ ╶╴ 15 ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ 15 ╶╴ ╶╴   15 ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   
╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   
╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ 30            ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ 31   ╶╴ ╶╴ 31               
╶╴ 31                                                                                       

   September 2022          October 2022          November 2022          December 2022       
Mo Tu We Th Fr Sa Su   Mo Tu We Th Fr Sa Su   Mo Tu We Th Fr Sa Su   Mo Tu We Th Fr Sa Su   
         ╶╴ ╶╴ ╶╴ ╶╴                  ╶╴ ╶╴      ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴            ╶╴ ╶╴ ╶╴ ╶╴   
╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   
╶╴ ╶╴ ╶╴ 15 ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ 15 ╶╴   ╶╴ 15 ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ 15 ╶╴ ╶╴ ╶╴   
╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   
╶╴ ╶╴ ╶╴ ╶╴ 30         ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ 30               ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ 31      
                       31                                                                   

--------------------------------------------------------------------------------------------

    January 2023          February 2023            March 2023             April 2023        
Mo Tu We Th Fr Sa Su   Mo Tu We Th Fr Sa Su   Mo Tu We Th Fr Sa Su   Mo Tu We Th Fr Sa Su   
                  ╶╴         ╶╴ ╶╴ ╶╴ ╶╴ ╶╴         ╶╴ ╶╴ ╶╴ ╶╴ ╶╴                  ╶╴ ╶╴   
╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   
╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ 15   ╶╴ ╶╴ 15 ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ 15 ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ 15 ╶╴   
╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   
╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ 28                  ╶╴ ╶╴ ╶╴ ╶╴ 31         ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ 30   
╶╴ 31                                                                                       

      May 2023              June 2023              July 2023             August 2023        
Mo Tu We Th Fr Sa Su   Mo Tu We Th Fr Sa Su   Mo Tu We Th Fr Sa Su   Mo Tu We Th Fr Sa Su   
╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴            ╶╴ ╶╴ ╶╴ ╶╴                  ╶╴ ╶╴      ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   
╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   
15 ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ 15 ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ 15 ╶╴   ╶╴ 15 ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   
╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   
╶╴ ╶╴ 31               ╶╴ ╶╴ ╶╴ ╶╴ 30         ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ 31            
                                              31                                            

   September 2023          October 2023          November 2023          December 2023       
Mo Tu We Th Fr Sa Su   Mo Tu We Th Fr Sa Su   Mo Tu We Th Fr Sa Su   Mo Tu We Th Fr Sa Su   
            ╶╴ ╶╴ ╶╴                     ╶╴         ╶╴ ╶╴ ╶╴ ╶╴ ╶╴               ╶╴ ╶╴ ╶╴   
╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   
╶╴ ╶╴ ╶╴ ╶╴ 15 ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ 15   ╶╴ ╶╴ 15 ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ 15 ╶╴ ╶╴   
╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   
╶╴ ╶╴ ╶╴ ╶╴ ╶╴ 30      ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ 30            ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ 31   
                       ╶╴ 31                                                                

--------------------------------------------------------------------------------------------

    January 2024          February 2024            March 2024             April 2024        
Mo Tu We Th Fr Sa Su   Mo Tu We Th Fr Sa Su   Mo Tu We Th Fr Sa Su   Mo Tu We Th Fr Sa Su   
╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴            ╶╴ ╶╴ ╶╴ ╶╴               ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   
╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   
15 ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ 15 ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ 15 ╶╴ ╶╴   15 ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   
╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   
╶╴ ╶╴ 31               ╶╴ ╶╴ ╶╴ 29            ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ 31   ╶╴ 30                  

      May 2024              June 2024              July 2024             August 2024        
Mo Tu We Th Fr Sa Su   Mo Tu We Th Fr Sa Su   Mo Tu We Th Fr Sa Su   Mo Tu We Th Fr Sa Su   
      ╶╴ ╶╴ ╶╴ ╶╴ ╶╴                  ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴            ╶╴ ╶╴ ╶╴ ╶╴   
╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   
╶╴ ╶╴ 15 ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ 15 ╶╴   15 ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ 15 ╶╴ ╶╴ ╶╴   
╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   
╶╴ ╶╴ ╶╴ ╶╴ 31         ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ 30   ╶╴ ╶╴ 31               ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ 31      

   September 2024          October 2024          November 2024          December 2024       
Mo Tu We Th Fr Sa Su   Mo Tu We Th Fr Sa Su   Mo Tu We Th Fr Sa Su   Mo Tu We Th Fr Sa Su   
                  ╶╴      ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴               ╶╴ ╶╴ ╶╴                     ╶╴   
╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   
╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ 15   ╶╴ 15 ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   
╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   
╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   ╶╴ ╶╴ ╶╴ ╶╴            ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴      ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴ ╶╴   
30                                                                   ╶╴ ╶╴                  
```

## Test

```sh
python3 -m unittest -v test_calendar_prettifier.py
```

```txt
test_format_multiyear_range (test_calendar_prettifier.TestDateRangePrettifier) ... ok
test_format_multiyear_selected_year (test_calendar_prettifier.TestDateRangePrettifier) ... ok
test_format_singleyear_range (test_calendar_prettifier.TestDateRangePrettifier) ... ok
test_format_singleyear_selected_year_not_in_range (test_calendar_prettifier.TestDateRangePrettifier) ... ok
test_format_year_different_structure (test_calendar_prettifier.TestDateRangePrettifier) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.053s

OK
```
