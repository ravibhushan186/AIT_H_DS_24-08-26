'''
Inheritance:
Inheritance is an OOP concept in which a child class acquires the properties and methods of a parent class.
                                    OR
A class can inherites the properties and methods avalible in or declared in other class

'''

'''
1. Simple/ Single Inheritance: 
When one child class inherits from one parent class, it is called single inheritance.

2. Multiple Inheritance:
When one child class inherits from two or more parent classes, it is called multiple inheritance.

3. Multi-level Inheritance:
When a class inherits from another class, and a further class inherits from that child class, it is called multilevel inheritance.

4. Hierarchical inheritance:
When two or more child classes inherit from the same parent class, it is called hierarchical inheritance.

5. Hybrid Inheritance:
When two or more types of inheritance are combined in a single class structure, it is called hybrid inheritance.

'''

# ************1. Simple/ Single Inheritance***********

# class parent:
#     def __init__(self):
#         self.name = "Chirangivee"
#     def job(self):
#         print("He is an actor")

# class child(parent):
#     def __init__(self):
#         super().__init__()
#         self.cname = "Ram Charana"
#     def occ(self):
#         print("He is a Business man")

# c = child()
# print(c.name)
# c.job()
# print(c.cname)
# c.occ()

# ***************2. Multiple Inheritance**********
# class Father:
#     def __init__(self, fage):
#             self.fage = fage

#     def drive(self):
#         print(f"Father: Driving (Age: {self.fage})")

# class Mother:
#     def __init__(self,mage):
#         self.mage = mage

#     def cooking(self):
#         print(f"Mother: cooking (Age: {self.mage})")

# class child(Father, Mother):
#     def __init__(self, fage, mage, cage):
#         #  super().__init__(fage)
#         Father.__init__(self, fage)
#         Mother.__init__(self, mage)
#         self.cage = cage

#     def skill(self):
#         print(f"Child: coding (Age: {self.cage})")

# c = child(55,50,24)

# c.drive()
# c.cooking()
# c.skill()

# *****************************3. multilevel inheritance.**********************
# class Grand:
#     def __init__(self):
#         self.gname = 'ANR'
#     def work(self):
#         print('He is an Actor')

# class Father(Grand):
#     def __init__(self):
#         super().__init__()
#         self.fname = 'NAG'
#     def job(self):
#         print("Actor com Business Man")

# class child(Father):
#     def __init__(self):
#         super().__init__()
#         self.cname = 'Chaitnya'
#     def occ(self):
#         print('Actor com Resturant Owner')

# c = child()
# print(c.gname)
# c.work()
# print(c.fname)
# c.job()
# print(c.cname)
# c.occ()

# If i want to pass the value to the constructor into the same code 

# class Grand:
#     def __init__(self,gname):
#         self.gname = gname
#     def work(self):
#         print('He is an Actor')

# class Father(Grand):
#     def __init__(self, gname, fname):
#         super().__init__(gname)
#         self.fname = fname
#     def job(self):
#         print("Actor com Business Man")

# class child(Father):
#     def __init__(self, gname, fname, cname):
#         super().__init__(gname, fname)
#         self.cname = cname
#     def occ(self):
#         print('Actor com Resturant Owner')

# c = child('ANR', 'NAG', 'chaityna')
# print(c.gname)
# c.work()
# print(c.fname)
# c.job()
# print(c.cname)
# c.occ()


# ******************4. Hierarchical inheritance:**************
# class parent:
#     def __init__(self, pname):
#         self.pname = pname

# class chil1(parent):
#     def __init__(self, pname, c1name):
#         super().__init__(pname)
#         self.c1name = c1name

# class child2(parent):
#     def __init__(self, pname, c2name):
#         super().__init__(pname)
#         self.c2name = c2name

# c1 = chil1('NAG', 'Chaitnaya')
# c2 = child2('NAG', 'Akhil')

# print(c1.pname)
# print(c1.c1name)
# print(c2.pname)
# print(c2.c2name)

# *******************5. Hybrid Inheritance:********************

class Father:
    def skills1(self):
        print("Father: Driving")

class Mother:
    def skills2(self):
        print("Mother: Cooking")

class Son(Father):
    def skills3(self):
        print("Son: Coding")

class Daughter(Father):
    def skills4(self):
        print("Daughter: painting")

class Child(Son, Mother):
    def skills5(self):
        print("child: playing")

c = Child()

c.skills1()
c.skills2()
c.skills3()
c.skills5()