
class EmployeeInvoker:

    def submit(self, command, daysWorked):
        return command.execute(daysWorked)