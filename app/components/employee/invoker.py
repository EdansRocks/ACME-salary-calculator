class EmployeeInvoker:
    def submit(self, command, days_worked):
        return command.execute(days_worked)
