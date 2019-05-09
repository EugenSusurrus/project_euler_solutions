"""
You are given the following information, but you may prefer to do some research for yourself.

    * 1 Jan 1900 was a Monday.
    * Thirty days has September, April, June and November.
    * All the rest have thirty-one,
    * Saving February alone,
    * Which has twenty-eight, rain or shine.
    * And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

import pandas as pd
import datetime as dt

start_date = dt.date(1901, 1, 1)
end_date = dt.date(2000, 12, 31)

date_range = pd.date_range(start_date, end_date)

first_of_the_month_saturdays_count = 0

for date in date_range:
    week_day_num = date.weekday()
    day_date = date.day

    if week_day_num == 6 and day_date == 1:
        first_of_the_month_saturdays_count += 1

print(first_of_the_month_saturdays_count)