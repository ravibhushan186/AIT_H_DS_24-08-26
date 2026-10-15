
def Account_Detail(i):

    try:
        print("Name:", i['NAME'])
        print("Username:", i['USERNAME'])
        print("Balance:", i['BALANCE'])

    except KeyError:
        print("Information missing")