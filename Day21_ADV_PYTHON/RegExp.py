'''
findall()
search()
match()
fullmatch()
sub
'''
import re

# pat = 'ab'
# string = 'ab'

# a= re.fullmatch(pat, string)
# print(a)
# print(a.span())
# print(a.group())

# pat = 'python'
# string='python is easy to read'
# res = re.match(pat, string)
# print(res)
# print(res.span())
# print(res.group())

# pat = 'can'
# string = 'can can can be cat'
# r = re.findall(pat, string)
# print(r)

# pat = 'python'
# string = 'currently i ma learning python'

# r = re.search(pat, string)
# print(r)
# print(r.span())
# print(r.group())

# sub is use to replace the pattern
pat = 'python'
string = 'java is easy to learn'

r = re.sub('java', pat, string)
print(r)