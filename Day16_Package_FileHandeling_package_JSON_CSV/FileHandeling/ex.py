'''
r  - read
w  - write
a  - append
r+ - readwrite
w+ - writeread
a+ - appendread
rb - readbinary
wb - writebinary
'''

# ------------'w' for Write --------------------

# f= open('sample.txt', 'w')
# print(f.writable())
# f.write('''
#     Johny Johny,
#     Yes Papa,
#     Eating Sugar?
#     No Papa
#     Are you sure
#     Yes Papa
#     Open your mouth
#     Ha, ha, ha
# ''')
# f.writelines(['Hi there!\n',
#               'How are you doing\n',
#               'I am doing fine\n',
#               'Currently i am learning python'])
# f.close()

# -------------'r' Read-----------------------
f=open('sample.txt', 'r')
# print(f.readable())

# data = f.read()
# print(data)

# data = f.readline()
# print(data)

# data = f.readlines()
# print(data)
# print(f.tell()) #count character
# f.seek(10) # Character place 
# print(f.tell())
# f.close()


# -------- 'a' append--------------------
# f=open('sample.txt','a')
# f.write('\nIt is easy to learn')
# f.close()

# --------------- With -----------------

with open('sample.txt', 'r') as f:
    data = f.read()
    print(data)

# NOTE: With the help of with method here no need to close the file