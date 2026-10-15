import re
email = r'[\w\W]+[a-z]+(.com)$'
gmail = 'ravibhushan2025@gmail.com'

res = re.fullmatch(email, gmail)
print(res)