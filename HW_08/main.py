from functions import *
from menu import *
import os



file = "phone_book.txt"
open_or_create_file(file)
enter = 4
while enter != 0:
    enter = menu()
    if enter == 1:
        user_name = str(input("Please enter name: "))
        user_surname = str(input("Please enter surname: "))
        user_ph_number = str(input("Please enter phone number: "))
        add_contact(file, user_name, user_surname, user_ph_number)

    elif enter == 2:
        print(show_all(file))

    elif enter == 3:
        request = str(input("Search: "))
        search(file, request)

print("\nWish all the best ;)")