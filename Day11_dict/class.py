'''
dict:
'''
d={1:'int', 12.5:'float', True:'bool', False:'Boolean', 'name':'string', 'tuple':(1,2), 
   'List':[1,2,3,4], 'set':{1,2,3,4},'dict':{1,2,3,4,5}}
# print(type(d))
# print(d)

# for i in d:
#     print(i)

# R = dict(name = "Ravi", age = 22, country = "India")
# print(R) 

# TypeError: unsupported operand type(s) for +: 'dict' and 'set' (it can't support the operand data types)
# d2={1,2,3,4,5,66,7}
# sum=d+d2
# print(sum)

# print(type(d))
# d1={'one':'ACE','two':'Dos','three':'threse'}

# for i in d:
#     print(i)

# zip
# enumarate

# l=[[1,'one'],[2,'two'],[3,'three']]
# l1=[(1,'one'),(2,'two'),(3,'three')]

# d=dict(l1)
# print(d)

# l=[1,2,3,4]
# l1=['one','two','three','four']

# d=dict(zip(l,l1))
# print(d)

# d=dict(enumerate(l1,101))
# print(d)

# d={}
# print(type(d))

# s=set()
# print(type(s))

# d={1:'one',2:'two',3:'three',4:'four'}

# print(d[1])
# d[1]='ACE'
# print(d)
# d[5]='five'
# print(d)

# print(dir(dict))
'''
'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
'''

# d1={}
# dic=d1.fromkeys(d)
# print(dic)

# # print(d.get(6))

# print(d.keys())
# print(d.values())
# print(d.items())

# d.pop(5)
# print(d)
# d.popitem()
# print(d)
# d.update({4:'four'})
# print(d)

# d.clear()
# print(d)
# del(d)
# print(d)

# l=[1,2,3,4,5]
# l1=['one','two','three','four','five']
# l2=[(1,'one'),(2,'two'),(3,'three'),(4,'four'),(5,'five')]

# d={x:y for x,y in l2}
# print(d)

# d1={x:y for x,y in zip(l,l1)}
# print(d1)

# d2={x:y for x,y in enumerate(l1,101)}
# print(d2)
