
from data import Customer


def SignUp():
    try:
        Name = input("Enter your name: ")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        confirm_password = input("Enter your confirm_password: ")

        if password == confirm_password:

            balance = float(input("Enter opening balance amount: "))

            if balance < 0:
                print("Invalid balance amount")
                return

            users = {
                'NAME': Name,
                'USERNAME': username,
                'PASSWORD': password,
                'BALANCE': balance
            }

            Customer.append(users)

            print("Registration Successful!")

        else:
            print("Password doesn't match!")

    except ValueError:
        print("Please enter a valid amount")