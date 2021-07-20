from ...common.interface import Command


class CalculateSalary(Command):
    def __init__(self, employee_receiver):
        self._employee_receiver = employee_receiver

    def execute(self, days_worked):
        return self._employee_receiver.calculate_salary(days_worked)

    def redo(self, days_worked):
        self.execute(days_worked)
