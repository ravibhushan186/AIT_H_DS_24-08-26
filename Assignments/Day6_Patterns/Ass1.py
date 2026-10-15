"""
A
AB
ABC
ABCD
ABCDE
"""
i = 1

while i <= 5:
    j = 0

    while j > i:
        print(chr(65 + j), end="")
        j += 1

    print()
    i += 1




'''
A
B C
D E F
G H I J
K L M N O
'''


# pyramid

# i=1
# while i<6:
#     print(' '*(5-i)+'* '*i)
#     i+=1


# print(chr(65))
# print(chr(66))
# print(chr(67))
# print(chr(68))