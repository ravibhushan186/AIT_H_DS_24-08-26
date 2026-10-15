'''
What is interface?
interface is a abstract class which contains only 
abstract method but not any normal method

NOTE:
1). We can't create object of interface
2). We use interface when an action is common but 
implementaion

3).All child class should be inherits abstract method


# Syntax:
import abc
class interface_class(ABC):
    @abstractmethod
    def fun(self):
        pass
    
    @abstractmethod
    def fun2(self)
        pass
'''

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def Show(self):
        pass

class Square(Shape):
    def Show(self):
        print("Square has 4 sides")

class Circle(Shape):
    def Show(self):
        print("Circle has round shape")

obj = Square()
obj1 = Circle()

obj.Show()
obj1.Show()