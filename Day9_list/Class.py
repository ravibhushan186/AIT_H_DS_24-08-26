''' 
List: is a mutable ordered collection of heterogeneous elements (Group of words)
It will allow duplicate values and it is represented by square brackets [].

'''

# l=[12,34.5,True,12+9j,'AchieversIT',12,True]
# print(type(l))
# print(l)

# l = list("Python")
# print(type(l))
# print(l)

# l1 = [1, 2, 3, 4, 5]
# l1[0] = 11
# print(l1)

# print(dir(list))


# l=list('python')
# print(l)

# l1=list((1,2,3,4,5,6))
# print(l1)
# l2=list({1,2,3,4,5,6,7,8,9,10,1})
# print(l2)
# l3=[1]
# print(l3)
l4=[]
print(type(l4))

# CRUD Slicing: It is used to access the elements of a list. It is done by using the index of the elements. The index starts from 0.
#l=[1,2,3,4,5,6,7,8]
# l[0]=10
# print(l)

# l2=l[::-1]
# print(l2)

# l[0:0]=[9]
# print(l)

# l[10:10]=[15]
# print(l)

# l[1:4]=[11]
# print(l)

# l[2:2]=[9,9,9]
# print(l)

# print(l[0:4])

# del(l[0])
# print(l)

'''
Adding
append
extend
insert

Deleting:
pop
clear
remove

finding:
index
count

sortting
sort

revense:
reverse

copying:
copy
'''

l=[1,2,3,4,5,6,7,8,9,10]
# l.append(11) #This method is used to add an element at the end of the list.
# print(l)

# l.extend([12,13,14,15]) #This method is used to add multiple elements at the end of the list.
# print(l)

# l.insert(1,0) #This method is used to add an element at a specific index. It takes two arguments, the first argument is the index and the second argument is the element to be added.
# print(l)

# l.pop() #This method is used to remove an element from the list. It takes an optional argument, the index of the element to be removed. If no index is provided, it removes the last element.
# print(l)

# l.pop(2) #This method is used to remove an element from the list. It takes an optional argument, the index of the element to be removed. If no index is provided, it removes the last element.
# print(l)

# l.remove(10) #
# print(l)

#print(l.index(2))

# l1=[1,2,1,3,4,5,6,5,7,8,6]
# print(l1.count(1)) #This method is used to count the number of occurrences of an element in the list. It takes one argument, the element to be counted.

# l.sort(reverse=True) #This method is used to sort the elements of the list in ascending order. It takes an optional argument, reverse, which is a boolean value. If reverse is True, the list is sorted in descending order.
# print(l)

l1=l
# print(id(l))
# print(id(l1))

# l1.pop()
# print(l1)
# print(l)

# l2=l.copy()
# print(id(l))
# print(id(l2))

# print(sum(l))
# print(min(l))
# print(max(l))

# l.clear()
# print(l)



# l=[x**2 for x in range(1,11)] # This is a list comprehension that creates a list of squares of numbers from 1 to 10.
# print(l)

# l=[[1,2,3],[4,5,6],[7,8,9]]
# print(l[1][2])
   