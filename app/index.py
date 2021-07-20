from .components import *
from .common import *
from .test import *


def calculate(path_file):
    """Calculate the payment amount for each user"""
    users = get_users_from_file(path_file)
    if users == None:
        print(
            "Error loading data! Please check that all employee information is correct\n"
        )
        return

    for user in users:
        payment = get_user_payment(user[1])
        if payment == None:
            print("Error loading " + user[0] + " info! Some days are incorrect!")
            return

        print("We must pay " + user[0] + ": " + str(payment) + "$")

    return


def enter_file_name():
    """Enter the file name"""
    file_name = "Non-existing-file"
    if __name__ == "app.index":

        file_name = input(
            "Please, write the name of the file in public/data folder (example: employees): \n"
        )

    return file_name


def get_user_payment(days_worked):
    """Get the payment amount for an user"""
    payment = 0
    if __name__ == "app.index":
        receiver = Employee()
        command = CalculateSalary(receiver)
        invoker = EmployeeInvoker()
        payment = invoker.submit(command, days_worked)

    return payment


def get_users_from_file(path_file):
    """Get all the users info from file"""
    users = []
    if __name__ == "app.index":
        receiver = File()
        command = ReadUsers(receiver)
        invoker = FileInvoker()
        users = invoker.submit(command, path_file)

    return users


def is_correct_file(path_file):
    """Check if the file exists"""
    is_correct_file = False
    if __name__ == "app.index":
        receiver = File()
        command = FileExists(receiver)
        invoker = FileInvoker()
        is_correct_file = invoker.submit(command, path_file)

    return is_correct_file


def load_file(path_file):
    """Load the file and set its extension .txt"""
    correct_file = False
    if __name__ == "app.index":
        path_file = set_txt_extension_file(path_file)
        if is_correct_file(path_file):
            correct_file = True
            calculate(path_file)

    return correct_file


def present_operations():
    """Present operations to user"""
    option = 0
    if __name__ == "app.index":
        print("Please, choose an option from below: \n")
        print("1. Use a custom file in public/data folder")
        print("2. Use default example file")
        print("0. Exit \n")
        option = input()

    return option
