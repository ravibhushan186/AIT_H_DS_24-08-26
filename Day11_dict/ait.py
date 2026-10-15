'''
dict:

'''
# d={1:'int',
#    12.49:'float',
#    True:'bool',
#    False:'Bool',
#    12+9j:'complex',
#    'List':[1,2,3,4],
#    'tuple':(1,2,3,4),
#    'set':{1,2,3,4},
#    }
# print(type(d))
# print(len(d))
# print(d["List"])
# print(d.get("List"))
# print(d.keys())
# print(d.values())



# d1={'one':'ACE','two':'Dos','three':'threse'}
# print(d1)

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

d={1:'one',2:'two',3:'three',4:'four'}

# print(d[1])
# d[1]='ACE'
# print(d)
# d[5]='five'
# print(d)

# print(dir(dict))

d1={}
d1.fromkeys(d)
print(d1)

print(d.get(6))

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

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
#  }
# # thisdict.update({"year": 2020})
# # print(thisdict)

# for x in thisdict:
# #   print(x)
#   print(thisdict[x])