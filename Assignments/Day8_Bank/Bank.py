'''
Develop a banking application where the user has to create a name, username, and password. The user should also enter a confirm password.
If the password and confirm password match, the application should display the account balance. The user should then be able to deposit and withdraw money from the account balance.
If the password and confirm password do not match, the application should display an error message.

## Registration
Name
Username
Password
Confirm password
Balance


#Login
username
password

#After login
    1. Check Account Balance
    2. Deposit
    3. Withdraw
    4. logout

'''

#Registration

Name = input("Enter your name: ")
username = input("Username: ")
password = input("Password: ")
confirmPassword = input("Confirm Password: ")

if password == confirmPassword:
    print("Registation Succesful")
    balance = 0
else:
    print("Password does not match")


#Login
USERNAME = input("Enter your username: ")
PASSWORD = input("Enter your password: ")

if USERNAME == username and PASSWORD == password:
    print("Login Successful")
else:
    print("Invalid username or password")

#After login
while True:
    print('''chose an option:
    1. Check Account Balance
    2. Deposit
    3. Withdraw''')

    select = int(input("Enter your choice: "))
    if select == 1:
        print("Your account balance is:",balance)

    elif select == 2:
        deposit = int(input("Enter amount to deposit: "))
        balance += deposit
        print("Deposit successful. New balance:", balance)

    elif select == 3:
        withdraw = int(input("Enter amount to withdraw: "))
        if withdraw <= balance:
            balance -= withdraw
            print("Withdrawal successful. New balance:", balance)
        else:
            print("Insufficient balance")
    else:
        print("Invalid choice. Please try again.")
