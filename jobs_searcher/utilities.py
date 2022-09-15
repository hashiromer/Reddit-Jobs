"""Module for shared utility classes and functions required by all modules"""

from datetime import datetime
import pytz


def parsez_datetime(date:str, timezone="Asia/Karachi")->datetime:
    """
    Takes datetime as string and returns datetime object with a given timezone
    """
    number_date=int(date)
    time_zone=pytz.timezone(timezone)
    submission_date=datetime.fromtimestamp(number_date,tz=time_zone)
    return submission_date