
def Balance_Enquiry(i):

    try:
        print("Balance:", i['BALANCE'])

    except KeyError:
        print("Balance information is missing")