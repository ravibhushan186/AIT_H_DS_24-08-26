'''
Encapsulation:
Encapsulation is an OOP concept in which data (variables) and methods (functions) are combined into a 
single unit called a class, while controlling access to the data.

public : accessible from anywhere.
protected : intended for use inside the class and its subclasses.
private : intended for use only inside the class.
'''
#************* Public******************
# class public:
#     def __init__(self, name):
#         self.name = name
#     def display(self):
#         print(self.name)

# s = public("Ravi")
# # s.display()

# s.name = 'Bhushan'
# print(s.name)

# **************Protected**************
# class protected:
#     def __init__(self, _name): # Here _name is use to protect the data but you can modify and acces the data from child class also
#         self._name = _name
#     def display(self):
#         print(self._name)

# class child(protected):
#     def show(self):
#         print("This is a child class")

# c = child('Ravi')
# # print(c._name)
# c._name = 'Bhushan'
# print(c._name)


# ****************Private****************
# class private:
#     def __init__(self, __name):
#         self.__name = __name
#     def display(self):
#         print(self.__name)

# class child(private):
#     def show(self):
#         print("This is a child class")

# s = private("Ravi")
# print(s.__name) #It is not accessable using this cos of __name it is in private mode
# s.display() #This is accessable using calling display method

# s._private__name = 'Bhushan' ##name mangaling
# s.display()

# getter and setter method to access the private outputs

# class private:
#     def __init__(self, __name):
#         self.__name = __name
#     def get(self):
#         print(self.__name)
#     def set(self, rename):
#         self.__name = rename

# class child(private):
#     def show(self):
#         print("This is a child class")

# s = private('Ravi')
# s.get()
# s.set('Bhushan')
# s.get()