from .components import *
from .common import *
from .test import *

""" Calculate the payment amount for each user """
def calculate(pathFile):
    users = getUsersFromFile(pathFile)
    
    if(users == None):
        print('Error loading data! Please check that all employee information is correct\n')
        return

    for user in users:
        payment = getUserPayment(user[1])

        if(payment == None):
            print('Error loading ' + user[0] + ' info! Some days are incorrect!')
            return 

        print('We must pay ' + user[0] + ': ' + str(payment) + '$')

    return

""" Enter the file name """
def enterFileName():
    fileName = 'Non-existing-file'

    if (__name__ == 'app.index'):

        fileName = input('Please, write the name of the file in public/data folder: \n')
    
    return fileName

""" Get the payment amount for an user """
def getUserPayment(daysWorked):
    payment = 0

    if (__name__ == 'app.index'):
        receiver = Employee()
        command = CalculateSalary(receiver)
        invoker = EmployeeInvoker()
    
        payment = invoker.submit(command, daysWorked)

    return payment

""" Get all the users info from file """
def getUsersFromFile(pathFile):
    users = []

    if (__name__ == 'app.index'):
        receiver = File()
        command = ReadUsers(receiver)
        invoker = FileInvoker()
    
        users = invoker.submit(command, pathFile)

    return users

""" Check if the file exists """
def isCorrectFile(pathFile):
    isCorrectFile = False

    if (__name__ == 'app.index'):
        receiver = File()
        command = FileExists(receiver)
        invoker = FileInvoker()
    
        isCorrectFile = invoker.submit(command, pathFile)

    return isCorrectFile

""" Load the file and set its extension .txt """
def loadFile(pathFile):
    correctFile = False

    if (__name__ == 'app.index'):
        pathFile = setTxtExtensionFile(pathFile)

        if(isCorrectFile(pathFile)):
            correctFile = True
            calculate(pathFile)

    return correctFile

""" Present operations to user """
def presentOperations():
    option = 0

    if (__name__ == 'app.index'):
        print('Please, choose an option from below: \n')
        print('1. Use a custom file in public/data folder')
        print('2. Use default example file')
        print('0. Exit \n')

        option = input()
    
    return option