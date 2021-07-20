from ...payment_config import *
from ...common.utils import *


class Employee:
    def calculate_salary(self, days_worked):
        """
        CS - Calculate the salary of an employee based on days worked
        param daysWorked: list - List of the days the employee has worked
        return: Integer - The payment amount for that employee
                None - If the info is not correct
        """
        payment_amount = 0
        for day in days_worked:
            daily_payment = 0
            payment_method = DAYS_OF_WEEK.get(day[0].upper(), -1)
            correct_info = self.__check_integrity(payment_method, day[1])
            if not correct_info:
                return

            start, end = day[1].split("-")
            start, end = convert_to_dates(start, end)
            hours = get_hours_worked(start, end)
            schedule = check_schedule(start, end)
            if schedule >= 0:
                daily_payment = PAYMENT[payment_method][schedule] * hours
            else:
                daily_payment = self.__calculate_payment_between_schedules(
                    payment_method, start, end
                )

            payment_amount += daily_payment

        return payment_amount

    def __calculate_payment_between_schedules(self, payment_method, start, end):
        """
        Calculate the payment if the employee has worked between different schedules
        param paymentMethod: Integer - The payment method for that day
        param start: datetime - The datetime at which the employee started work
        param end: datetime - The datetime at which the employee finished work
        return: Integer - The payment amount for that employee
        """
        daily_payment = 0
        for schedule in SCHEDULES:
            schedule_dates = get_schedule_dates(schedule)
            dates = self.__get_correct_dates(start, end, schedule_dates)
            if not dates == None:
                first, second = dates
                hours = get_hours_worked(first, second)
                daily_payment += PAYMENT[payment_method][schedule] * hours

        return daily_payment

    def __get_correct_dates(self, start, end, schedule_dates):
        """
        Check the correct dates between two schedules
        param start: datetime - The datetime at which the employee started work
        param end: datetime - The datetime at which the employee finished work
        param scheduleDates: List - Schedule start and end datetimes
        return: Datetime - Correct datetimes when the employee has worked
        """
        start_schedule, end_schedule = schedule_dates
        is_correct_start = check_between_dates(start_schedule, end_schedule, start)
        if is_correct_start:
            return start, end_schedule

        is_correct_end = check_between_dates(start_schedule, end_schedule, end)
        if is_correct_end:
            return start_schedule, end

        is_correct_schedule = check_between_dates(
            start, end, start_schedule, end_schedule
        )
        if is_correct_schedule:
            return start_schedule, end_schedule

        return

    def __check_integrity(self, payment_method, worked_schedule):
        """
        Check if the information of the user is correct
        param paymentMethod: Integer - The payment method for that day
        param: workedSchedule - The schedule the employee worked
        return: Boolean - True if the info is correct otherwise False
        """
        if payment_method == -1:
            return False

        if len(worked_schedule.split("-")) < 2:
            return False

        start, end = worked_schedule.split("-")
        if not check_date_string(start) or not check_date_string(end):
            return False

        return True
