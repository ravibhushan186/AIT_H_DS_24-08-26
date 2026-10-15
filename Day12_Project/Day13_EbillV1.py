Admin=[]
users=[]
bills=[]

while True:
    print('''**** Welcome to Ebill ****
            1. Admin Registation
            2. Admin Login
            3. Exit
''')
    choice = input("Enter your choice: ")
    match choice:
        case 1:
            username = input("Enter Your username: ")
            password = input("Enter Your Password: ")
            Cpassword = input("Enter Your Confirm Password: ")

            if password == Cpassword:
                data = {'username':username, 'password':password}
                Admin.append(data)
                print("Registation successful")
            else:
                print("Password not matched")
        case 2:
            USERNAME = input("Enter your username: ")
            PASSWORD = input("Enter your password: ")

            if i in Admin:
                if i['USERNAME'] == USERNAME and i['PASSWORD'] == PASSWORD:
                    print("Login succesful")

                    while True:
                        print('''**** Dashboard ****
                                1. User Registation
                                2. User Login
                                3. Create Bill
                                4. View Bills
                                5. Logout
''')
                        choose = input("Choose any of them: ")
                        match choose:
                            case 1:
                                uname = input("Enter username: ")
                                pword = input("Enter password: ")
                                cpass = input("Confirm password: ")

                                if pword == cpass:
                                    detail={'uname': uname, 'cpass': cpass}
                                    users.append(detail)
                                    print("User created")
                                else:
                                    print("Password not matched")

                            case 2:
                                UNAME = input('Enter your username: ')
                                PWORD = input("Enter your password: ")

                                for j in users:
                                    if j['UNAME'] == UNAME and j['PWORD'] == PWORD:
                                        print("User login successful")
                                    else:
                                        print('djaubfaef')
                            case 3:
                                username = input("Enter your username: ")
                                for k in users:
                                    if k['username'] == username:
                                        units = float(input("Enter units: "))
                                        rate=9
                                        amount = units*rate
                                        data={'username':username, 'units':units, 'rate':rate, 'amount':amount}
                                        bills.append(data)
                                        print("Bill created")
                                        print("Amount: ",amount)
                                    
                                    else:
                                        print("User not found")

                            case 4:
                                print("Bill")

                                for b in bills:
                                    print(b)

                            case 5:
                                print("Logout")
                                break

                            case _:
                                print("Invalid choice")
                    break
                else:
                    print("invalid admin username or password")

        case 3:
            print("Thank you for using Ebill")
            break
        case _:
            print("Invalid choice")        