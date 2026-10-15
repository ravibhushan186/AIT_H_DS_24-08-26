'''
Polymorphism:
Polymorphism is an OOP concept in which the same method or interface can perform different behaviors 
depending on the object or context.
                                OR
Polymorphism means ability to take various form (Same object having diffrent behaviours)


'''

# print(5+5) # It is adding a value
# Output: 10
# print("5"+"5") # it is concatnating a value 
# Output: 55
#NOTE: Here the print() object is same but the working of the object is diffrent that is one is adding the value and anothe r one is concanating the value

'''
Polymorphism Types:
1. Overloading:
Whenever class contains more that one methods with 
same name and diffrent types parameters called overloading


2. Overriding:
whenever we writing method name with same signature in 
parent & child class known as method overriding

'''
# ****************Method Overloading ******************
# class A:
#     def show(self):
#         print("Welcome")

#     def show(self, firstname=''):
#         print("Welcome", firstname)

#     def show(self, firstname='', lastname=''):
#         print(f"Welcom ", firstname ,lastname)

# obj = A()
# obj.show()
# obj.show('Ravi')
# obj.show("Ravi","Bhushan")

# ********************Method Overriding ****************

class Father:
    def work(self):
        print("Father is working")

class Child(Father):
    def work(self):
        print("Child is coding")

obj = Child()
obj.work()

# f = Father()
# f.work()

# NOTE: In the child and parent class have same name of method then the child class have the first prority to print there method it's override 

# If we remove the work() method from the child class does
# child calss use the father's work() method..

# c = Child()
# c.work()
