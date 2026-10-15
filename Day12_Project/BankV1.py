Customer = []
while True:
    print(''' **** Welcome to PythonBank ****
            1. Sign Up
            2. Sign In
            3. Log Out
''')
    choice = int(input("Enter your choice: "))
    match choice:
        # SIGN UP
        case 1:
            Name = input("Enter your Name: ")
            username = input("Enter your username: ")
            password = input("Enter Password: ")
            confirm_Password = input("Re-enter Password: ")

            if password == confirm_Password:
                balance = float( input("Enter the opening balance amount: "))

                users = {'NAME': Name,'USERNAME': username,'PASSWORD': password,'BALANCE': balance}
                Customer.append(users)
                print("Registration Successful!")
            else:
                print("Password doesn't match!")

        # SIGN IN
        case 2:
            USERNAME = input("Enter your username: ")
            PASSWORD = input("Enter Password: ")
            for i in Customer:
                if i['USERNAME'] == USERNAME and i['PASSWORD'] == PASSWORD:
                    print("Sign In Successful!")

                    # After SING IN
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
                                print("Name:", i['NAME'])
                                print("Username:", i['USERNAME'])
                                print("Balance:", i['BALANCE'])
                            case 2:
                                print("Balance:", i['BALANCE'])
                            case 3:
                                deposit = float(input("Enter your Deposit Amount: "))
                                if deposit > 0:
                                    i['BALANCE'] += deposit
                                    print("Deposit Successful!", i['BALANCE'])
                                else:
                                    print("Invalid Amount!")
                            case 4:
                                withdrawal = float(input("Enter amount to withdraw: "))
                                if withdrawal > 0:
                                    if withdrawal <= i['BALANCE']:
                                        i['BALANCE'] -= withdrawal
                                        print("Withdrawal Successful! ", i['BALANCE'])
                                    else:
                                        print("Insufficient Balance!")
                                else:
                                    print("Invalid Amount!")
                            case 5:
                                print("Logged out successfully!")
                                break
                            case _:
                                print("Invalid Choice!")
                    break
        case 3:
            print("Thank you for using PythonBank!")
            break
        case _:
            print("Invalid Choice!")