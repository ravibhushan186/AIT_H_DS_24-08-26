'''
instance Variables
class Variables
instance Method
static methods
class method

Decorator: A decorator is a function that modifies or extends the behavior of another function or method without changing its original code.
                                                OR
Decorator = A function that adds extra functionality to another function.


'''

class Math:
    name = "Ravi" ## class Variables
    age = 24 ## class Variables

    def __init__(self, a, b):
        self.a = a #instance variables.
        self.b = b # instance variables.

    def add(self): # instance Method
        return self.a + self.b
    def diff(self): # instance Method
        return self.a - self.b
    def pro(self): #instance Method
        return self.a * self.b
    @staticmethod
    def about(): # static methods / enq method
        print("This method is known as static methods")

    @classmethod
    def intro(cls):
        print("This method is known as class methods")

print(Math.name) # It is access the class Variables

m1 = Math(10,5) # This is an object
print(m1.add())
print(m1.diff())
print(m1.pro())
Math.about()
Math.intro()