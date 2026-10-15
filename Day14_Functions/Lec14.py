'''
Nested Function = function inside function
closure function: When the inner function have the ability to read the outer functions variables and parameters
Higher order function
Call back function: if a fun invoking from another function and executing it's proisor then it is called as call back function
'''
# def outer():
#     print("This statement belong to outer functions")
#     def inner():
#         print("This statement belongs to inner function")
#     # inner()
#     return inner
# # outer()
# outer()()


# closure function
# def outer(a,b):
#     name="Ravi"
#     print(f"The value of a is {a} and b is {b} belongs to outer function")
#     def inner():
#         print(a+b,name)
#     inner()
# outer(10,2)


# Higher order function

# def Sample(f): ##Higher order function
#     print('*'*10)
#     f()
#     print('*'*10)

# def greeting(): ##Call back function
#     print("Hello World")
# Sample(greeting)

# Lambda function:
# res=(lambda x:x**2)
# print(res(25))

# add=(lambda x,y:x+y)
# print(add(10,2))

# print((lambda x: x*10)(10))

# l=[1,2,3,4,5]
# res = map((lambda x:x**2),l)
# print(res)

# for i in res:
#     print(i)