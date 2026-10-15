
from account import Account_Detail
from balance import Balance_Enquiry
from deposit import Deposit
from withdrawal import Withdrawl


def menu(i):

    while True:

        try:

            print('''
            **** PythonBank ****
            1. Account Detail
            2. Balance Enquiry
            3. Deposit
            4. Withdrawal
            5. Exit
            ''')

            choice = int(input("Enter your choice: "))

            match choice:

                case 1:
                    Account_Detail(i)

                case 2:
                    Balance_Enquiry(i)

                case 3:
                    Deposit(i)

                case 4:
                    Withdrawl(i)

                case 5:
                    print("Logout")
                    break

                case _:
                    print("Invalid choice")

        except ValueError:
            print("Please enter valid input")