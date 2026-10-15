'''
Class: A class is a blueprint of template that defines agroup of related variables(data) and methods(behavior)
Object: An object is an instance of a class. It represents a real-world entity and can access the attributes and methods defined in the class.
inheritance:
encapsulation:
Abstraction:
polymorphism:
'''

# NOTE: classes are nothing but first class functions
class Sample:
    def __init__(self): ## Instance
        self.name = "Ravi"
        self.age = "24"

    def greet(self):
        print(f"Hello {self.name} you are {self.age} years old")

s = Sample()
s.greet()