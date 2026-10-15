from customer import customer

class PythonBank:
    def __init__(self):
        self.CUSTOMER = []

    def sign_up(self):
        name = input("Enter your name: ")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        confirm_password = input("Re-enter your password: ")

        if password == confirm_password:
            balance = float(input("Enter your openaning balance amount: "))

            user = customer(name, username, password, balance)
            self.CUSTOMER.append(user)

            print("Registation successfu")
        else:
            print("Password does not match: ")

    def Sign_in(self):
            USRERNAME = input("Enter your username: ")
            PASSWORD = input("Enter your password:")
    
            for i in self.CUSTOMER:
                if i.username == USRERNAME and i.password == PASSWORD:
                    print("Sign-in successful")
                    self.menu(i)
                    break
                else:
                    print("Invalid username and passsword")

    def menu(self, i):
        while True:
            print('''
                    **** PythonBank ****
                    1. Account Detail
                    2. Balance Enquiry
                    3. Deposit
                    4. Withdrawal
                     5. Exit

''')
            choice = input("Please enter your choice: ")
            match choice:
                case 1:
                    i.Account_Detail()
                case 2:
                    i.Balance_Enquiry()
                case 3:
                    i.Deposit()
                case 4:
                    i.Withdrawal()
                case 5:
                    break
                case _:
                    print("Please enter valid input")
