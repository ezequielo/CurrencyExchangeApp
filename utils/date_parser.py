import datetime
import re

from dateutil.relativedelta import relativedelta
from django.utils import timezone

HOLIDAYS = [
            # 2013
            datetime.date(2013, 1, 1),
            datetime.date(2013, 3, 29),
            datetime.date(2013, 4, 1),
            datetime.date(2013, 5, 6),
            datetime.date(2013, 5, 27),
            datetime.date(2013, 8, 26),
            datetime.date(2013, 12, 25),
            datetime.date(2013, 12, 26),
            # 2014
            datetime.date(2014, 1, 1),
            datetime.date(2014, 4, 18),
            datetime.date(2014, 4, 21),
            datetime.date(2014, 5, 5),
            datetime.date(2014, 5, 26),
            datetime.date(2014, 8, 25),
            datetime.date(2014, 12, 25),
            datetime.date(2014, 12, 26),
            # 2015
            datetime.date(2015, 1, 1),
            datetime.date(2015, 4, 3),
            datetime.date(2015, 4, 6),
            datetime.date(2015, 5, 4),
            datetime.date(2015, 5, 25),
            datetime.date(2015, 8, 31),
            datetime.date(2015, 12, 25),
            datetime.date(2015, 12, 28),
            ]

def is_business_date(date):
    if isinstance(date, datetime.datetime):
        date = date.date()

    if date.weekday() == 5 or date.weekday() == 6:
        return False
    if date in HOLIDAYS:
        return False
    return True


def add_business_days(date, days):
    """Add #days business days to date."""
    end_date = date
    counter = 0
    while counter < days:
        end_date += datetime.timedelta(days=1)
        if is_business_date(end_date):
            counter += 1

    return end_date


def add_business_days_backward(date, days):
    """Add #days business days to date."""
    end_date = date
    counter = 0
    while counter < days:
        end_date -= datetime.timedelta(days=1)
        if is_business_date(end_date):
            counter += 1

    return end_date


def get_date(date):
    """
    Transforms one date expressed in natural language in the corresponding `datetime.datetime` object.

    It accepts one of these expressions (most of them take now as initial datetime):
        - today: now
        - yesterday: subtracts one day
        - tomorrow: adds one day
        - a week ago: subtracts one week
        - within a week: adds one week
        - X month(s) ago: subtracts X month(s)
        - X day(s) ago: subtracts X day(s)
        - X business day(s) ago: subtracts X business day(s), it doesn't count weekends and holidays
        - within X business day(s): adds X business day(s), it doesn't count weekends and holidays
        - mm/dd/yyyy: date indicated in format day/month/year
    :param date: Date expressed in natural language
    :type date: str
    :return: Date converted in datetime object if matches one of the possibilities
    :rtype: datetime.datetime or None
    """
    date = date.lower()
    now = timezone.now()

    if 'midnight' in date:
        now = datetime.datetime.combine(now, datetime.time(0, 0, 0, 0))

    if 'today' in date:
        return now

    if 'yesterday' in date:
        return now - datetime.timedelta(days=1)

    if 'tomorrow' in date:
        return now + datetime.timedelta(days=1)

    if date == 'a week ago':
        return now - datetime.timedelta(days=7)

    if date == 'within a week':
        return now + datetime.timedelta(days=7)

    if re.search("\d+ months? ago", date):
        num_month = int(date.split(' ')[0])
        return now - relativedelta(months=num_month)

    if re.search("\d+ minutes ago", date):
        num_minutes = int(date.split(' ')[0])
        date = datetime.datetime.now() - datetime.timedelta(minutes=num_minutes)
        return date

    if re.search("\d+ days? ago", date):
        num_days = int(date.split(' ')[0])
        return now - datetime.timedelta(days=num_days)

    rm = re.match("^(\d+) business days? ago$", date)
    if rm:
        num_days = int(rm.groups(1)[0])
        return add_business_days_backward(now, num_days)

    if re.search("within \d+ business days?", date):
        num_days = int(date.split(' ')[1])
        return add_business_days(now, num_days)

    if re.match("^\d{1,2}/\d{1,2}/\d{4}$", date):
        return datetime.datetime.strptime(date, "%d/%m/%Y")

    if re.match("^\d{1,2}/\d{1,2}/\d{4} \d{1,2}:\d{1,2}$", date):
        return datetime.datetime.strptime(date, "%d/%m/%Y %H:%M")

