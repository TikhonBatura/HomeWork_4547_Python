import os

def open_or_create_file (fName):
    try: 
        objct = open(fName, 'r')
    except IOError:
        print('New list have been created -> phone_book.txt')
        objct = open(fName, 'w')
    finally:
        objct.close()

def add_contact(file, user_name, user_surname, user_ph_number):
    os.system('CLS') # очистка консоли
    data = open(file, 'a')
    data.write(user_name + " " + user_surname + " " + user_ph_number + "\n")
    data.close()

def show_all(file): # показывает всех абонентов и позволяет редактировать список

    os.system('CLS') # очистка консоли
    data = open(file, "r")
    for line in data:
        print(line[:-1])
    data.close()

    input("Press Enter to continue...\n")
    flag = False
    
    while flag != True:
        print("===Change / Delete menu===")
        print("\nPress 1 to change contatct data\nPress 2 to delete contatct\nPress 0 back to main menu\n")
        user_choise = int(input("\nPlease chouse would you like to do: "))
        
        if user_choise == 1:
            print("Which contact would you like to change?")
            user_input = input()
            change(file, user_input)
            show_all(file)
            flag = True

        if user_choise == 2:
            print("Which contact would you like to delete?")
            user_input = input()
            delete_contact(file, user_input)
            show_all(file)
            flag = True

        if user_choise == 0:
            flag = True

    data.close()


def search(file, user_input):
    a = 0
    os.system('CLS') # очистка консоли
    data = open(file, 'r')
    for line in data:
        if user_input in line:
            print(line)
            a = 123
            break
    
    if a != 123:
        print("Nothing founded")
    input("Press Enter to continue...\n")
    data.close()

def change(file, abDATA):
    with open(file, "r+") as data1:
        contents = data1.read()
        new_value = input('Enter new value: ')
        contents = contents.replace(abDATA, new_value)    
        with open(file, "w") as data2:
                data2.write(contents)
        input("Press Enter to continue...")


def delete_contact(file, old_value):
    with open(file, "r+") as data1:
        contents = data1.read().splitlines()
        for line in contents:
            if old_value in line:
                contents.remove(line)
           
            with open(file, "w") as data2:
                for i in contents:
                    data2.write(i)
                    data2.write('\n')
        input("Press Enter to continue...")