#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import MAXYEAR, MINYEAR, date, datetime, time, timedelta
from time import mktime, monotonic, sleep, strptime

from dateutil import parser
from dateutil.relativedelta import relativedelta
from dateutil.rrule import FR, HOURLY, SU, WEEKLY, rrule
from runner.koan import *


class AboutDateTime(Koan):
    """
        These koans are based on python's 'datetime' library.
    """

    def test_year_range(self):
        self.assertEqual(__, MINYEAR)
        self.assertEqual(__, MAXYEAR)

    def test_date_object_range(self):
        """
        date is an object of (YEAR, MONTH, DAY).
        Range of each argument is as following:
            MINYEAR <= YEAR <= MAXYEAR
            1 <= MONTH <= 12
            1 <= DAY <= number of days in the given month and year

        If date doesn't fall in range, raises ValueError
        """
        self.assertEqual(__, type(date.min))
        self.assertEqual(date(__, __, __), date.min)
        self.assertEqual(date(__, __, __), date.max)
        with self.assertRaises(__):
            date(2018, 12, 35)

    def test_time_object_range(self):
        """
        time is an object of (hour, minute, second, microsecond, tzinifo).
        All arguments are optional, tzinfo (timezone) maybe None (default value).
        All default to 0 except tzinfo.
        Range of each argument is as following:
            0 <= hour < 24
            0 <= minute < 60
            0 <= second < 60
            0 <= microsecond < 1000000

        If time doesn't fall in range, raises ValueError
        """
        self.assertEqual(__, type(time.min))
        self.assertEqual(time(__, __, __, __), time.min)
        self.assertEqual(time(__, __, __, __), time.max)
        with self.assertRaises(__):
            time(23, 60, 12, 199)

    def test_datetime_object_range(self):
        """
        datetime is an object of (YEAR, MONTH, DAY, hour, minute, second, microsecond, tzinfo)
        """
        self.assertEqual(datetime(__, __, __, __, __, __, __), datetime.min)
        self.assertEqual(datetime(__, __, __, __, __, __, __), datetime.max)

    def test_calculate_time_difference(self):
        # timedelta object represents a duration, the difference between two dates or times in the format of
        # (days, seconds, microseconds, milliseconds, minutes, hours, weeks)
        #
        # Range of attributes:
        #   -999999999 <= days <= 999999999
        #   0 <= seconds <= 86399
        #   0 <= microseconds <= 999999

        year = timedelta(days=365)
        another_year = timedelta(weeks=51, days=7, hours=23, minutes=60)  # adds upto 365 days
        self.assertEqual(__, year == another_year)
        self.assertEqual(__, year - another_year)

        # Calculate a date for 30 days after 'year'
        self.assertEqual(__, year + timedelta(days=30))

        # Date for next Friday
        # Weekdays are represented from number 0 to 6, where 0 being Monday and 6 being Sunday.
        # So Friday will be 4.
        today = date(2018, 9, 6)  # 6 Sep 2018
        next_friday = today + timedelta((4 - today.weekday()) % 7)
        self.assertEqual(__, next_friday.day)

        # Last tuesday's day (wrt 'today')
        self.assertEqual(__, 4)

        # For time differences, we can also use 'relativedelta' class of 'dateutil' library
        # Next month
        next_month = today + relativedelta(months=+1)
        self.assertEqual(__, next_month.month)
        # Next friday
        self.assertEqual(__, (today + relativedelta(weekday=FR)).day)
        # It is easier to handle datetime differences using relativedelta.
        # Last friday of month. To calculate last friday of month we have to specify that how many maximum number of
        # days can be in a month, then take out the last friday entry.
        self.assertEqual(__, (today + relativedelta(day=31, weekday=FR(-1))).day)

        # Calculate the datetime before a month, plus one week, at 1pm from 'today'
        self.assertEqual(__, datetime(2018, 7, 30, 13, 0))

        # time.monotonic: Returns the value (in fractional seconds) of a monotonic clock,
        # i.e. a clock that cannot go backwards.
        # Perform a sanity check
        is_monotonic = True
        if monotonic() - monotonic() > 0:
            # monotonic() is not monotonic
            is_monotonic = False
        self.assertEqual(__, is_monotonic)

        start_time = monotonic()
        # do something or code logic in here, i.e. suspending execution for 1sec
        sleep(1)  # sleep for 1sec
        end_time = monotonic()
        # Now 'end_time - start_time' gives correct elapsed time, even if system clock changes
        self.assertEqual(__, end_time - start_time >= 1)

    def test_datetime_as_string_format(self):
        """
        Converts datetime object into string format, if not able to parse object in given format raises ValueError.
        """
        dummy_date = date(2018, 9, 6)
        # strftime(format) method creates a string representation for the datetime objects based on a given format.
        self.assertEqual(__, dummy_date.strftime("%d-%m-%Y"))
        # %A is for full weekday's name, %B is for full month's name
        self.assertEqual(__, dummy_date.strftime("%d %B %Y, %A"))

        dummy_time = time(13, 45, 24)
        # time in 24-hour clock format
        self.assertEqual(__, dummy_time.strftime("%H:%M:%S"))
        # time in 12-hour clock format
        self.assertEqual(__, dummy_time.strftime("%I:%M:%S %p"))
        # Insert literal character '%'
        self.assertEqual(__, '01 % 45 % 24')

        with self.assertRaises(__):
            # 'Q' is not a known parsing argument
            dummy_time.strftime("%Q")

    def test_convert_string_to_datetime(self):
        """
        Converts string into a struct_time/datetime object representing datetime, if fails to parse in given format
        raises ValueError.
        """
        dummy_date = '06-09-2018'
        # strptime(format) method converts a string representation of datetime into a struct_time object.
        self.assertEqual(__, strptime(dummy_date, "%d-%m-%Y").tm_year)
        self.assertEqual(__, strptime('06 Sep 18', "%d %b %y").tm_mon)

        with self.assertRaises(__):
            strptime(dummy_date, "%d-%b-%Y")

        # Parse date like these
        #   December 12th 2017 and January 1st 2017
        #
        # We can parse first date with pattern: '%B %dth %Y'
        self.assertEqual(__, strptime('December 12th 2017', "%B %dth %Y").tm_mday)
        # Now try the same pattern for second date
        try:
            strptime('January 1st 2017', "%B %dth %Y")
        except Exception as ex:
            err_msg = ex.args[0]

        self.assertRegex(__, err_msg)

        # Second date cannot be parsed with the same pattern/format because of 'th' and 'st' difference.
        # For this kind of dates, you can use dateutil.parser (http://labix.org/python-dateutil)
        # dateutil.parser.parse method will return a datetime.datetime object.
        self.assertEqual(__, parser.parse('January 1st 2017'))

        # Get 'month' from date: December 2nd 2017 and December 1st 2017
        self.assertEqual(__, parser.parse('December 2nd 2017').month)
        # Raises Exception if unable to parse
        with self.assertRaises(__):
            parser.parse('December 32nd 2017')  # out of range date

    def test_timezone_information(self):
        """
        About timezone information datetime object.
        """
        from pytz import timezone
        # Local time in 'IST' timezone
        local_time = datetime(2018, 9, 6, 14, 53, 0, tzinfo=timezone('Asia/Kolkata'))
        time_in_utc_tz = local_time.astimezone(timezone('UTC'))
        self.assertEqual(__, local_time - time_in_utc_tz)

        # Let us calculate the difference between times by excluding timezones
        local_time = local_time.strftime("%d-%m-%Y %H-%M-%S")
        local_time = strptime(local_time, "%d-%m-%Y %H-%M-%S")
        time_in_utc_tz = time_in_utc_tz.strftime("%d-%m-%Y %H-%M-%S")
        time_in_utc_tz = strptime(time_in_utc_tz, "%d-%m-%Y %H-%M-%S")

        # Difference between IST(Asia/Kolkata) and UTC timezones using datetime object is 5:53 hrs
        # or 5:53 hrs = (5*3600) + (53*60) = 21180 seconds
        self.assertEqual(__, (mktime(local_time) - mktime(time_in_utc_tz)))

        # To get the real difference, which is 5:30 hrs (19800 seconds), we will have to use localize
        # See: http://bytes.com/topic/python/answers/676275-pytz-giving-incorrect-offset-timezone for more info
        current_time = datetime(2018, 9, 6, 14, 53, 0)
        IST = timezone('Asia/Kolkata')
        UTC = timezone('UTC')
        local_time = IST.localize(current_time)
        time_in_utc_tz = UTC.localize(current_time)
        self.assertEqual(__, (time_in_utc_tz - local_time).seconds)


    def test_recurrence_rules(self):
        """
        'rrule' class of 'dateutil' library provides a small, complete and very fast implementation of recurrence rules.
        """
        today = datetime(2018, 9, 6)
        # Next 2 years from now which has 53 weeks. We have to provide a weekday, based on that weeks will be
        # calculated.
        next_year_with_53_weeks = list(rrule(WEEKLY, byweekno=53, byweekday=SU,
                                             dtstart=today + relativedelta(years=+1), count=2))
        self.assertEqual(__, [i.year for i in next_year_with_53_weeks])

        # Every 7 hrs in the current day 'today'
        every_7_hrs = list(rrule(HOURLY, interval=7, dtstart=today,
                                 until=today + relativedelta(days=+1)))
        self.assertEqual(__, [i.hour for i in every_7_hrs])

        # Find every 51st monday of the year from 'today' for 3 occurrences in YYYY-mm-dd format.
        self.assertEqual(__, ['2018-12-17', '2019-12-23', '2020-12-21'])
