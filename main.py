#!/usr/bin/env python
from messages_config import *
from app import index


def main(restart):
    """Main"""
    execute = {"0": exit, "1": custom_file, "2": example_file}
    if restart:
        print(WRONG_OPTION)
        print("Invalid Option! Please Choose one correctly \n")
    option = index.present_operations()
    step = execute.get(option, lambda: main(True))
    return step()


def custom_file():
    """Option custom file"""
    fileName = index.enter_file_name()
    path = FILES_PATH + fileName
    execute(path)
    return


def example_file():
    """Option example file"""
    path = FILES_PATH + "test_example.txt"
    execute(path)
    return


def execute(path):
    """Execute app with specific file"""
    print("\n")
    all_correct = index.load_file(path)
    if not all_correct:
        print(ERROR)
        print("Error Loading File!, Please check if the file name is correct \n")
    else:
        print(GOODBYE)
    return


def exit():
    """Option exit"""
    print(GOODBYE)
    return


if __name__ == "__main__":
    print(PRESENTATION)
    main(False)
