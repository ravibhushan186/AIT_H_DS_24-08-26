
def Deposit(i):

    try:
        Damount = float(input("Enter your Deposit Amount: "))

        if Damount > 0:

            i['BALANCE'] += Damount

            print("Deposit Successful", i['BALANCE'])

        else:
            print("Invalid amount")

    except ValueError:
        print("Please enter valid amount")