
def Withdrawl(i):

    try:
        Wamount = float(input("Enter amount to withdraw: "))

        if Wamount > 0:

            if Wamount <= i['BALANCE']:

                i['BALANCE'] -= Wamount

                print("Withdrawal Successful", i['BALANCE'])

            else:
                print("Insufficient Balance")

        else:
            print("Invalid Amount")

    except ValueError:
        print("Please enter valid input")