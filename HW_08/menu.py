import os

def menu():
    os.system('CLS')
    print("====MAIN MENU====")
    print(" 1 - add contact \n 2 - show all (change / delete data) \n 3 - Search \n 0 - exit\n")
    enter = int(input("Please chouse whould you like to do: "))
    return enter