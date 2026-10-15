'''
w+
r+
a+

rb
wb
'''

 ## -----'w+' Write + read ---------
# with open('sample.txt', 'w+') as f:
#     data='''Hi there \nGood morning\ntoday is a beautiful day'''
#     f.write(data)
#     f.seek(0)
#     result = f.read()
#     print(result)

# -----'r+' read + write

# with open('sample.txt','r+') as f:
#     data = f.read()
#     add = '\nLets go for a ride'
#     f.write(add)
#     f.seek(0)
#     total = f.read()
#     print(f.tell)
#     print(data)
#     print(total)

# ------ 'a+' append + read, write
# with open('sample.txt', 'a+') as f:
#     print(f.tell())
#     add = '\n and have a good lunch'
#     f.write(add)
#     f.seek(0)
#     data = f.read()
#     print(data)
#     print(f.tell())

# ---- 'rb' read binary--------

medium = None
with open('msi.jpg','rb') as f:
    medium=f.read()
    print(medium)

with open('Laptop.jpg','wb') as f:
    f.write(medium)




    