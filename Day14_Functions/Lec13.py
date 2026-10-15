'''
def nameoffunction():
    block of code

nameoffunction()

1. simple Function
2. Function with parameters
3. Function with return statement
4. Function with multiple return statements
5. Function with position only arrguments
6. Function with keyword only arguments
7.function with mixed positional and keyword arguments
8. Function with variable length positional arguments
9. Function with variable length keyword argumnets
'''

# def sample():
    # print("Hello world")
    # return "Hello world"

# sample()

# for i in range(1,3):
#     sample()

# customer = []

# for i in range(1,3):
#     customer.append(sample())

# print(customer)

# def add(a,b): #Formal parameters / arguments
#     return a+b
# print(add(20,10)) # Actual parameters/arrguments

# def math(a,b):
#     print(f"a is {a} and b is {b}")
#     sum=a+b
#     diff=a-b
#     pro=a*b
#     div=a/b
#     mod=a%b
#     intdiv=a//b

#     return (f"sum={sum}, diff={diff}, pro={pro}, div={div}, mod={mod}, intdiv={intdiv}")

# print(math(10,2))
# print(math(b=10, a=2))
# print(math(10, b=2))


# def add(a,b,c,/):
#     return a,b,c

# print(add(10,20,30))

# def add(*,a,b,c):
#     return a+b+c

# print(add(c=20,b=23,a=7))


# def add(a,b,/,*,c,d):
#     return a+b+c+d

# print(add(10,20,d=30,c=40))

# def add(*Ravi):
#     # print(Ravi)
#     out=0
#     for i in Ravi:
#         out+=i
#     return out

# print(add(10,20,30,40,50,60))


# def person_info(**kwargs):
#     # print(kwargs)
#     for i in kwargs:
#         print(f"{i}={kwargs[i]}")

# person_info(name="Ravi", age=24, occu="student")

def add(**kwargs):
    out=0
    for i in kwargs:
        out+=kwargs[i]
    return out
print(add(a=10,b=20,c=30,d=40))