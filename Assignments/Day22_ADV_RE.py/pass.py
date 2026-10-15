import re
length = r'[\w\W]{8,16}'
password = 'Bhushan@12345'

res = re.fullmatch(length, password)
print(res)