Customer = []
def SignUp():
    Name = input("Enter your Name: ")
    username = input("Enter your username: ")
    password = input("Enter Password: ")
    confirm_Password = input("Re-enter Password: ")

    if password == confirm_Password:
        balance = float(input("Enter the opening balance amount: "))
        users = {'NAME': Name,'USERNAME': username,'PASSWORD': password,'BALANCE': balance}
        Customer.append(users)
        print("Registration Successful!")
    else:
        print("Password doesn't match!")

def SingIn():
    USERNAME = input("Enter Your username: ")
    PASSWORD = input("Enter your password: ")
    for i in Customer:
        if i['USERNAME'] == USERNAME and i['PASSWORD'] == PASSWORD:
            print("Sign in Successful ")
            menu(i)
            break

def menu(i):
    while True:
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
                Withdrawal(i)
            case 5:
                print("Logged out successfully!")
                break
            case _:
                print("Invalid Choice")

def Account_Detail(i):
    print("Name:", i['NAME'])
    print("Username:", i['USERNAME'])
    print("Balance:", i['BALANCE'])

def Balance_Enquiry(i):
    print("Balance:", i['BALANCE'])

def Deposit(i):
    deposit_amount = float(input("Enter your Deposit Amount: "))
    if deposit_amount > 0:
        i['BALANCE'] += deposit_amount
        print("Deposit Successful!", i['BALANCE'])
    else:
        print("Invalid Amount!")

def Withdrawal(i):
    withdrawal_amount = float(input("Enter amount to withdraw: "))
    if withdrawal_amount > 0:
        if withdrawal_amount <= i['BALANCE']:
            i['BALANCE'] -= withdrawal_amount
            print("Withdrawal Successful!", i['BALANCE'])
        else:
            print("Insufficient Balance!")
    else:
        print("Invalid Amount!")

while True:
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
            SingIn()
        case 3:
            print("Thanks for using PythonBank")
            break
        case _:
            print("Invalid Choice")

