class customer:
    def __init__(self, name, username, password, balance):
        self.name = name
        self.username = username
        self.password = password
        self.balance = balance

    def Account_Details(self):
        print("Name: ", self.name)
        print("Username: ", self.username)
        print("Balance: ", self.balance)

    def Balance_Enquiry(self):
        print("Balance: ", self.balance)

    def Deposit(self):
        Damount = float(input("Enter your Deposite Amount: "))
        if Damount > 0:
            self.balance += Damount
            print("Deposite Successful")
            print("New Balance: ", self.balance)

    def Withdrawal(self):
        Wamount = float(input("Enter your Withdrawal Amount: "))
        if Wamount > 0:
            if Wamount <= self.balance:
                self.balance -= Wamount
                print("Withdrawal Successful")
                print("New Balance: ", self.balance)
            else:
                print("Insufficient balance")
        else:
            print("Please enter valid input")
            