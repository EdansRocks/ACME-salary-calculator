#!/usr/bin/env python
from messages_config import *
from app import index


""" Main """
def main(restart): 
    execute = {
        '0': exit,
        '1': customFile,
        '2': exampleFile
    }

    if (restart):
        print(WRONG_OPTION)
        print('Invalid Option! Please Choose one correctly \n')

    option = index.presentOperations()
    step = execute.get(option, lambda: main(True))

    return step()

""" Option custom file """
def customFile():
    fileName = index.enterFileName()
    path = FILES_PATH + fileName
    execute(path)
    return

""" Option example file """
def exampleFile():
    path = FILES_PATH + 'test_example.txt'
    execute(path)
    return

""" Execute app with specific file """
def execute(path):
    print('\n')
    allCorrect = index.loadFile(path)
    if(not allCorrect):
        print(ERROR)
        print('Error Loading File!, Please check if the file name is correct \n')
    else:
        print(GOODBYE)
    return

""" Option exit """
def exit():
    print(GOODBYE)
    return

if ( __name__ == '__main__'):
    print(PRESENTATION)
    main(False)
        

        
