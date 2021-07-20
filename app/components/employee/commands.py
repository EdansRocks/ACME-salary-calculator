from ...common.interface import Command

class CalculateSalary(Command):

    def __init__(self, employeeReceiver):
        self.employeeReceiver = employeeReceiver

    def execute(self, daysWorked):
        return self.employeeReceiver.calculateSalary(daysWorked)

    def redo(self, daysWorked):
        self.execute(daysWorked)

