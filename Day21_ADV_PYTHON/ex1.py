import re
'''
()
[]
^
$
[^]
'''

'''
Quantifiers
+ 1 or more
? 1 or none
* none or more
{m} exact count
{n,m} from n to till m
(n|m) it can be either n or m
'''

# pat = '(abc)+'
# string = 'abcabcabc' 

# r = re.fullmatch(pat,string)
# print(r)

# pat = '[abc]+'
# string = 'b' 

# r = re.fullmatch(pat,string)
# print(r)

# pat = '[abc]?'
# string = '' 
# string = 'a'

# r = re.fullmatch(pat,string)
# print(r)

# pat = '[abc]*'
# string = 'abcabcabc' 

# r = re.fullmatch(pat,string)
# print(r)

# ------------------------------------
# pat = '[a-zA-Z0-9]+'
# string = 'RaviBhushan12' 

# r = re.fullmatch(pat,string)
# print(r)

# Pan card pattern
# pat = '[A-Z]{5}[0-9]{4}[A-Z]{1}'
# pan_num = 'DHLAK1299A'

# res = re.fullmatch(pat,pan_num)
# print(res)




# ---------------------------
# pat = '[^A-Z]{5}[0-9]{4}[A-Z]{1}'
# pan_num = '!@#$%1234A' # Matched

# res = re.fullmatch(pat,pan_num)
# print(res)

# pat = '^[A-Z]{5}[0-9]{4}[A-Z]{1}$'
# pan_num = 'DHLAK1299A'

# res = re.fullmatch(pat,pan_num)
# print(res)

# ---------------------------------------------------------
'''
\d digit
\D non-digits
\w word character
\W non-word character
\s spaces
\S nonspaces
\. period
. Anychar

r => RawString
'''

# pat = r'\.'
# string = '.'

# res = re.fullmatch(pat,string)
# print(res)


# pat = r'\d+' # it allowed only digit
# string = '1234567890'

# res = re.fullmatch(pat,string)
# print(res)


# pat = r'\D+' #except digit it allowed anything
# string = 'wfajnfnwad@##$%^&'

# res = re.fullmatch(pat,string)
# print(res)


# pat = r'\w+' # either lower case and upper case including digits also
# string = 'qwertyuioQWERTYUIOP1234567'

# res = re.fullmatch(pat,string)
# print(res)



# pat = r'\s+'
# string = '         '

# res = re.fullmatch(pat,string)
# print(res)



# pat = r'\S+' #Except space it can be anything
# string = '12345qwertyQWERTYU@#$%^&'

# res = re.fullmatch(pat,string)
# print(res)

# pat = r'.+' # it accept any character
# string = '123456789qwertyuioQWERTYUIOP!@#$%^&*()'

# res = re.fullmatch(pat,string)
# print(res)


# phone = r'^[6-9]{1}\d{9}$'
# number = '7857864827'

# res = re.fullmatch(phone, number)
# print(res)