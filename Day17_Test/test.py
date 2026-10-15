'''

'''
# Q1
# x=10
# y=3
# print(x//y) # 3

# Q2
# tuple

# Q3
# x=10
# if x>5:
#     print("A") #A
# elif x > 8:
#     print("B")
# else:
#     print("c")

# Q4
# **

# Q5
# print(bool("")) #False

# Q6
# lower()

# Q7
# s="Python"
# print(s[1:4]) #yth

# Q8
# a=[1,2,4]
# a.append(5)
# print(a) # append


# Q9 
# b. Remove the last index

# Q10
# c. (10,20,30)

# Q11
# c. Dictionary

# Q12
# d={"name":"Ravi", "age":"24"}
# print(d["name"])  #Ravi

# Q13
# c. except

# Q14
# d). Finally

# Q15
# c). a

# Q16
# b). Existing content can be overwrite

# Q17
# a) json.load()

# Q18
# c). json.dump()

# Q19
# for i in range(1,5):
#     print(i) #1234

# Q20
# b). Stop the loop

# Q21
# x=15
# y=4
# print(x+y) #19
# print(x-y) # 11
# print(x*y)# 60
# print(x//y) #3
# print(x%y) #3

# Q22
# x=10
# if x % 2 == 0:
#     print("Even") #Even
# else:
#     print("Odd")

# Q23
# for i in range(2,10,2):
#     print(i, end=" ") #2 4 6 8


# Q24
# s="Python Programming"

# print(s.upper()) #PYTHON PROGRAMMING
# print(s.lower()) #python programming
# print(s.startswith("Python")) # True
# print(s.count("m")) #2


# Q25
# l=[10,20,30]

# l.append(40)
# print(l) # [10, 20, 30, 40]
# l.insert(1,15)
# print(l) # [10, 15, 20, 30, 40]
# l.remove(30)
# print(l) #[10, 15, 20, 40]

# Q26
# n = [1,2,2,3,3,3] 

# print(len(n)) # 6
# print(n.count(3)) # 3

# Q27
# d={
#     "name":"John",
#     "age":25
# }
# d["city"] = "Hyderabad"
# print(d) #{'name': 'John', 'age': 25, 'city': 'Hyderabad'}

# print(d.keys()) # dict_keys(['name', 'age', 'city'])

# Q28
# try:
#     a=10
#     b=0
#     print(a/b)
# except ZeroDivisionError:
#     print("Cannot divide by zero") #Cannot divide by zero
# finally:
#     print("Program completed") #Program completed

# Q29
# n = [10,20,30,40,50]

# for i in n:
#     if i == 30:
#         break
#     print(i) # 10 20

# Q30
# try:
#     x=int("100")
#     print(x+50) #150
# except ValueError:
#     print("Invalid value")

# Q31
# name = "Python"

# if name == "Python": # Error (:)
#     print(name)

# Q32
# num=[10,20,30]
# num.append(40) # Error is add
# print(num) # [10, 20, 30, 40]


# Q33
# try:
#     num = int(input("Enter number: ")) #100
#     print(num/100) #1.0
# except:
#     print("Invalid Input")


# Q34
# with open("data.txt","w") as f: # Error "r"
#     data = f.write("Hello")
#     print(data) # 5

# Q35
# import json
# data={
#     "namr":"Ravi",
#     "age":22
# }

# with open("student.json","w") as f:
#     json.dump(data,f)

# Q36
# num = "12345"
# print(num[::-1])

# Q37
# num = [10, 45, 23, 67, 12, 89, 34]
# l = num[0]
# s = num[0]

# for i in num:
#     if i > l:
#         s = l        
#         l = i        
#     elif i > s and i != l:
#         s = i
# print(s)  # Output: 67


# Q38
# f = "banana"
# print(f.count("b")) # 1
# print(f.count("a")) # 3
# print(f.count("n")) # 2


# Q39
# s1 = int(input("Enter marks for Subject 1: "))
# s2 = int(input("Enter marks for Subject 2: "))
# s3 = int(input("Enter marks for Subject 3: "))
# s4 = int(input("Enter marks for Subject 4: "))
# s5 = int(input("Enter marks for Subject 5: "))
# total = s1 + s2 + s3 + s4 + s5
# average = total / 5
# percentage = (total / 500) * 100 
# if percentage >= 90 and percentage <= 100:
#     grade = "A"
# elif percentage >= 75 and percentage < 90:
#     grade = "B"
# elif percentage >= 60 and percentage < 75:
#     grade = "C"
# elif percentage >= 40 and percentage < 60:
#     grade = "D"
# else:
#     grade = "Fail"

# print("Total Marks: ", total)
# print("Average Marks: ", average)
# print("Percentage: ", percentage)
# print("Grade: ", grade)


# ------------------------------------------------------------------------------------------------------------
# Q40
# import json
# {
#     "Students":[
#         {
#             "id":101,
#             "name":"Ravi",
#             "age":21,
#             "marks":85
#         },
#         {
#             "id":102,
#             "name":"James",
#             "age":21,
#             "marks":72
#         },
#         {
#             "id":103,
#             "name":"John",
#             "age":20,
#             "marks":91
#         }
#     ]
# }
# with open("students.json", "r") as f:
#     data = json.load(f)
#     students = data["Students"]
#     print(students)


# for student in "students":
#     print(student["name"])

# ------------------------------------------------------------------------------------------------------------
