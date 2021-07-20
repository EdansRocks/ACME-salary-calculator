from datetime import datetime, timedelta
from ...payment_config import *
import re


def check_between_dates(start, end, to_check_start, to_check_end=False):
    """
    CBD - Check if a datetime is between other two datetimes
    param start: datetime - Start datetime to check
    param end: datetime - End datetime to check
    param toCheckStart: datetime - Datetime to check if is in between
    param toCheckEnd: datetime - Datetime to check if is between(optional)
    return: Boolean - True if toCheckStart && toCheckEnd is between start and end otherwise false
    """
    if not to_check_end:
        return start <= to_check_start <= end
    else:
        return start <= to_check_start <= to_check_end <= end


def check_date_string(string):
    """
    CDS - Check if a string complies with the datetime format 'xx:xx'
    param string: String - Text with the date in string
    return: Boolean - True if match the format otherwise false
    """
    match = re.match("[0-9]{2}:[0-9]{2}$", string)
    return bool(match)


def check_schedule(start, end):
    """
    CS - Check if two datetimes are between an specific schedule in payment_config
    param start: datetime - First datetime to check if is in between an schedule
    param end: datetime - Second datetime to check if is in between an schedule
    return: Integer - Key of the schedule in payment_config otherwise -1
    """
    index = -1
    for schedule in SCHEDULES:
        start_schedule, end_schedule = get_schedule_dates(schedule)
        is_correct_schedule = check_between_dates(
            start_schedule, end_schedule, start, end
        )
        if is_correct_schedule:
            index = schedule
            return index

    return index


def convert_to_dates(start, end):
    """
    CTD - Convert two strings to datetimes in format 'xx:xx'
    param start: String - First string to convert
    param end: String - Second string to convert
    return: datetime - Two datetimes
    """
    start = datetime.strptime(start, "%H:%M")
    end = datetime.strptime(end, "%H:%M")
    if end < start:
        end += timedelta(days=1)

    return start, end


def get_hours_worked(start, end):
    """
    GHW - Get the hours worked between two datetimes
    param start: datetime - Start datetime
    param end: datetime - End datetime
    return: Int - Hours worked between start to end
    """
    time = end - start
    return round((time.seconds / 3600) + (time.days * 24))


def get_schedule_dates(schedule):
    """
    GSD - Get the start and end datetime from an schedule
    param schedule: Int - Key of the schedule in payment_config
    return: datetime - Two datetimes
    """
    start_schedule = SCHEDULES[schedule]["start"]
    end_schedule = SCHEDULES[schedule]["end"]
    start_schedule, end_schedule = convert_to_dates(start_schedule, end_schedule)

    return start_schedule, end_schedule


def set_txt_extension_file(file_path):
    """
    STEF - Set an .txt to an filepath
    param filePath: String - Path where the file is located
    return: String - New path with .txt extension
    """
    path = file_path
    if ".txt" not in file_path:
        path = file_path + ".txt"

    return path
