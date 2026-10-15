# class PythonBank:
#     def __init__(self): #constructor / decorator
#         self.CUSTOMER = []

#     def Sign_up(self):
#         name = input("Enter your Name: ")
#         username = input("Enter your username: ")
#         password = input("Enter Your Password: ")
#         confirm_password = input("Re-enter your password: ")

#         if password == confirm_password:
#             balance = float(input("Enter your openaning balance: "))

#             users = customer(name, username, password, balance)
#             self.CUSTOMER.append(users)
#             print("Registation successful")
#         else:
#             print("Password doesn't match")

#     def Sign_in(self):
#         USRERNAME = input("Enter your username: ")
#         PASSWORD = input("Enter your password:")

#         for i in self.CUSTOMER:
#             if i.username == USRERNAME and i.password == PASSWORD:
#                 print("Sign-in successful")
#                 self.menu(i)
#                 break
#             else:
#                 print("Invalid username and passsword")

#     def menu(self, i):
#         while True:
#             print('''
#                     **** PythonBank ****
#                     1. Account Detail
#                     2. Balance Enquiry
#                     3. Deposit
#                     4. Withdrawal
#                     5. Exit
#                     ''')
#             choice = int(input("Enter your choice: "))
#             match choice:
#                 case 1:
#                     i.Account_Detail()
#                 case 2:
#                     i.Balance_Enquiry()
#                 case 3:
#                     i.Deposit()
#                 case 4:
#                     i.Withdrawal()
#                 case 5:
#                     print("Exit")
#                     break
#                 case _:
#                     print("Invalid Choice")


#     def AIT(self):
#             while True:
#                 print('''
#                          ******** Welcome to PythonBank*************
#                          1.Sign_up
#                          2.Sign_in
#                          3.Sign_out
#     ''')
#                 choose = int(input("Please choose one of them: "))
#                 match choose:
#                     case 1:
#                         self.Sign_up()
#                     case 2:
#                         self.Sign_in()
#                     case 3:
#                         print("Thanks for using PythonBank")
#                         break
#                     case _:
#                         print("Please enter valid choice")
            
# class customer:
#     def __init__(self,name, username, password, balance):
#         self.name = name
#         self.username = username
#         self.password = password
#         self.balance = balance

#     def Account_Detail(self):
#         print("Name: ", self.name)
#         print("Username: ", self.username)
#         print("Balance: ", self.balance)

#     def Balance_Enquiry(self):
#         print("Balance: ", self.balance)
        
#     def Deposit(self):
#         Damount = float(input("Enter your Deposit Amount: "))

#         if Damount > 0:
#             self.balance += Damount
#             print("Deposite Successful")
#             print("New Balance: ",self.balance)
#         else:
#             print("Invalid Input")
#     def Withdrawal(self):
#         Wamount=(float(input("Enter Your Withdrawal Amount: ")))
#         if Wamount >0:
#             if Wamount <= self.balance:
#                 self.balance -= Wamount
#                 print("Withdrawal Successful")
#                 print("New Balance: ",self.balance)
#             else:
#                 print("Invalid amount")
# Bank = PythonBank()
# Bank.AIT()



# --------------------------------------------------------------------------------------------
'''
Parent class: User
Holds details about an users
Has a function to show users details
child class: Bank
store details about the acount balance
store details about the amount
Allowd for deposits, withdrawals, and balance enquiry
'''
class User: