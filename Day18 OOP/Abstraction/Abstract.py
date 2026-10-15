'''
What is abstract class?
Abstract class is class that contains one or more abstract method
is know as abstract class

NOTE: 
1). An object of an abstract class cannot be created
2). Python provides abc module to work with abstraction
3). We use @abstractmethod decoartor to define abstract method

Syntax:
from abc import ABC
class demo(ABC):
    def fun(self):
        body
    @abstractmethod
    def fun2(self):
'''
from abc import ABC, abstractmethod

class Car(ABC):
    def Show(self):
        print("Every car has 4 wheels")
    @abstractmethod
    def Speed(self):
        pass

class Tata(Car):
    def Speed(self):
        print("Maximum speed of the car is 120km/h")

class Suzuki(Car):
    def Speed(self):
        print("Maximum speed of the car is 100km/h")

obj = Tata()
obj.Show()
obj.Speed()

obj1 = Suzuki()
obj1.Show()
obj1.Speed()