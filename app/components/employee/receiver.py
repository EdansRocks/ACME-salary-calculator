from ...payment_config import *
from ...common.utils import *

class Employee:

    '''
    CS - Calculate the salary of an employee based on days worked
    param daysWorked: list - List of the days the employee has worked
    return: Integer - The payment amount for that employee
            None - If the info is not correct
    '''
    def calculateSalary(self, daysWorked):
        
        paymentAmount = 0

        for day in daysWorked:
            paymentMethod = DAYS_OF_WEEK.get(day[0].upper(), -1)

            correctInfo = self.__checkIntegrity(paymentMethod, day[1])
            if (not correctInfo):
                return
  
            start, end = day[1].split('-')
            start, end = convertToDates(start, end)
            
            hours = getHoursWorked(start, end)
            schedule = checkSchedule(start, end)
            if(schedule >= 0):
                dailyPayment = PAYMENT[paymentMethod][schedule] * hours
            else:
                dailyPayment = self.__calculatePaymentBetweenSchedules(paymentMethod, start, end)
                
            paymentAmount += dailyPayment
        
        return paymentAmount

    '''
    Calculate the payment if the employee has worked between different schedules
    param paymentMethod: Integer - The payment method for that day
    param start: datetime - The datetime at which the employee started work
    param end: datetime - The datetime at which the employee finished work
    return: Integer - The payment amount for that employee
    '''
    def __calculatePaymentBetweenSchedules(self, paymentMethod, start, end):
        
        dailyPayment = 0
        
        for schedule in SCHEDULES:
            scheduleDates = getScheduleDates(schedule)
            
            dates = self.__getCorrectDates(start, end, scheduleDates)
            
            if(not dates == None):
                first, second = dates
                hours = getHoursWorked(first, second)
                dailyPayment += PAYMENT[paymentMethod][schedule] * hours
            
        return dailyPayment

    '''
    Check the correct dates between two schedules
    param start: datetime - The datetime at which the employee started work
    param end: datetime - The datetime at which the employee finished work
    param scheduleDates: List - Schedule start and end datetimes
    return: Datetime - Correct datetimes when the employee has worked
    '''
    def __getCorrectDates(self, start, end, scheduleDates):

        startSchedule, endSchedule = scheduleDates

        isCorrectStart = checkBetweenDates(startSchedule, endSchedule, start)
        if(isCorrectStart):
            return start, endSchedule

        isCorrectEnd = checkBetweenDates(startSchedule, endSchedule, end)
        if(isCorrectEnd):
            return startSchedule, end

        isCorrectSchedule = checkBetweenDates(start, end, startSchedule, endSchedule)
        if(isCorrectSchedule):
            return startSchedule, endSchedule

        return

    '''
    Check if the information of the user is correct
    param paymentMethod: Integer - The payment method for that day
    param: workedSchedule - The schedule the employee worked
    return: Boolean - True if the info is correct otherwise False
    '''
    def __checkIntegrity(self, paymentMethod, workedSchedule):
  
        if (paymentMethod == -1):
            return False

        if (len(workedSchedule.split('-')) < 2):
            return False
        
        start, end = workedSchedule.split('-')

        if (not checkDateString(start) or not checkDateString(end)):
            return False

        return True