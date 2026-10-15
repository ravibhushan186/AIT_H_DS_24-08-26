'''
Function: reusable block of code can be utilized n no of times

types:
Builtin function
User-defined function

1.simple function
2.with parameters / arguments
3.with return statement
4.with multiple return statements
5. with default parameters
6. function with position only arguments
7.function with keyword only arguments
8.function with both positional and keyword arguments
9,function with variable length of positional arguments
'''
# def greetings():
#     print("Hello World ")
# greetings()

# def greet(person):
#     print('Hello World')

'''
def function_name(args/parameters):
    block of code
'''

# simple fucntion
# def greet():
#     print('Hello world')

# greet()
# greet()
# greet()


# def hello():
#     for i in range(1,11):
#         print(i)

# hello()     

# def hello(a):
#     return f'HI {a}'

# print(hello('james'))   


# def add(a,b):
#     print(a+b)

# add(10,20)    


'''
actual
formal
postiional
keyword
'''
# def add(a,b,c):
#     print(a+b+c)


# # add(10,20,30)
# # add(c=30,b=10,a=20)
# add(b=20,c=30,10)


# def add(a,b,/,*,c,d):
#     print(a,b,c,d)

# add(10,20,c=30,b=40)


# def add(a,b,c=1):
#     print(a+b+c)

# add(10,20,30)   

# variable length positional 

# def add(*args):
#     sum=0
#     for i in args:
#         sum+=i
#     print(sum)    

# add(10,20,30,40,50)
# add(10,20)
# add(10)    
