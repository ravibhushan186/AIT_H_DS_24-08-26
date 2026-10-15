
from signup import SignUp
from signin import SignIn


while True:

    try:

        print('''

        **** Welcome to PythonBank ****

        1. Sign Up
        2. Sign In
        3. Log Out

        ''')

        choice = int(input("Enter your choice: "))

        match choice:

            case 1:
                SignUp()

            case 2:
                SignIn()

            case 3:
                print("Thanks for using PythonBank")
                break

            case _:
                print("Invalid Choice")

    except ValueError:
        print("Please enter valid number")