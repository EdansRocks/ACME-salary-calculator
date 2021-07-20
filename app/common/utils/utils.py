from datetime import datetime, timedelta
from ...payment_config import *
import re

'''
CBD - Check if a datetime is between other two datetimes
param start: datetime - Start datetime to check
param end: datetime - End datetime to check
param toCheckStart: datetime - Datetime to check if is in between
param toCheckEnd: datetime - Datetime to check if is between(optional)
return: Boolean - True if toCheckStart && toCheckEnd is between start and end otherwise false
'''
def checkBetweenDates(start, end, toCheckStart, toCheckEnd = False):
    if (not toCheckEnd):
        return (start <= toCheckStart <= end)
    else:
        return (start <= toCheckStart <= toCheckEnd <= end)

'''
CDS - Check if a string complies with the datetime format 'xx:xx'
param string: String - Text with the date in string
return: Boolean - True if match the format otherwise false
'''
def checkDateString(string):
    match = re.match('[0-9]{2}:[0-9]{2}$', string)
    
    return bool(match)

'''
CS - Check if two datetimes are between an specific schedule in payment_config
param start: datetime - First datetime to check if is in between an schedule
param end: datetime - Second datetime to check if is in between an schedule
return: Integer - Key of the schedule in payment_config otherwise -1
'''
def checkSchedule(start, end):
    index = -1
    
    for schedule in SCHEDULES:
        startSchedule, endSchedule = getScheduleDates(schedule)
        
        isCorrectSchedule = checkBetweenDates(startSchedule, endSchedule,  start, end)
        if (isCorrectSchedule):
            index = schedule
            return index
    
    return index

'''
CTD - Convert two strings to datetimes in format 'xx:xx'
param start: String - First string to convert
param end: String - Second string to convert
return: datetime - Two datetimes
'''
def convertToDates(start, end):
    start = datetime.strptime(start, '%H:%M')
    end = datetime.strptime(end, '%H:%M')
    
    if(end < start):
         end += timedelta(days=1)
    
    return start, end

'''
GHW - Get the hours worked between two datetimes
param start: datetime - Start datetime
param end: datetime - End datetime
return: Int - Hours worked between start to end
'''  
def getHoursWorked(start, end):
    time = end - start
    return round((time.seconds / 3600) + (time.days * 24))

'''
GSD - Get the start and end datetime from an schedule
param schedule: Int - Key of the schedule in payment_config
return: datetime - Two datetimes
'''  
def getScheduleDates(schedule):
    startSchedule = SCHEDULES[schedule]['start']
    endSchedule = SCHEDULES[schedule]['end']
    startSchedule, endSchedule = convertToDates(startSchedule, endSchedule)
    
    return startSchedule, endSchedule

'''
STEF - Set an .txt to an filepath
param filePath: String - Path where the file is located
return: String - New path with .txt extension
'''
def setTxtExtensionFile(filePath):
    path = filePath

    if '.txt' not in filePath:
        path = filePath + '.txt'
    
    return path