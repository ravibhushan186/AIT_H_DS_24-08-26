Customer=[]

def SignUp():
    try:
        Name = input("Enter your name: ")
        username = input("Enter your username: ")
        password = input("ENter your password: ")
        confirm_password = input("Enter your confirm_password: ")

        if password == confirm_password:
            balance = float(input("Enter openaning balance amount: "))
            users = {'NAME': Name,'USERNAME': username,'PASSWORD': password,'BALANCE': balance}
            Customer.append(users)
            print("Registration Successful!")
        else:
            print("Password doesn't match!")
    except ValueError:
        print("Please enter a valid amount")

def SignIn():
    try:
        USERNAME = input("Enter your username: ")
        PASSWORD = input("Enter your password: ")

        for i in Customer:
            if i['USERNAME'] == USERNAME and i['PASSWORD'] == PASSWORD:
                print("SignIn Successful")
                menu(i)
                break
            print("Invalid username and password")
    except KeyError:
        print("Please enter valid input")


def menu(i):
    while True:
        try:
            print('''
            **** PythonBnak ****
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
                    print("Logout ")
                    break
                case _:
                    print("Inavlid choice")
        except ValueError:
            print("Plese enter valid input ")

def Account_Detail(i):
    try:
        print("Name:", i['NAME'])
        print("Username:", i['USERNAME'])
        print("Balance:", i['BALANCE'])
    except KeyError:
        print("Information missing")

def Balance_Enquiry(i):
    try:
        print("Balance: ", i['BALANCE'])
    except KeyError:
        print("Balance information is missing")
def Deposit(i):
    try:
        Damount = float(input("Enter your Deposit Amount: "))
        if Damount > 0:
            i['BALANCE'] += Damount
            print("Deposit Successful", i['BALANCE'])
        else:
            print("Invalid amount")

    except ValueError:
        print("Please enter vaalid amount")
def Withdrawl(i):
    try:
        Wamount = float(input("Enter amount to withdrawl: "))
        if Wamount > 0:
            if Wamount <= i['BALANCE']:
                i['BALANCE'] -= Wamount
                print("Withdrawl Successful", i['BALANCE'])
            else:
                print("Insufficient Balance")
        else:
            print("Invalid Amount")
    except ValueError:
        print("Please enter valid input")

while True:
    try:
        print(''' **** Welcome to PythonBank ****
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
