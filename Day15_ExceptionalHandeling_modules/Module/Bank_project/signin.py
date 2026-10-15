
from data import Customer
from menu import menu


def SignIn():

    USERNAME = input("Enter your username: ")
    PASSWORD = input("Enter your password: ")

    for i in Customer:

        if i['USERNAME'] == USERNAME and i['PASSWORD'] == PASSWORD:

            print("SignIn Successful")

            menu(i)

            return

    print("Invalid username and password")