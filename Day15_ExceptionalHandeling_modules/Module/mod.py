'''
What is a Module?
Consider a module to be the same as a code library.
A file containing a set of functions you want to include in your application.

Create a Module
To create a module just save the code you want in a file with the file extension .py:
'''

# import mymodule
# mymodule.greeting("Ravi Bhushan")
# #NOTE: When using a function from a module, use the syntax: module_name.function_name.

# import mymodule
# a = mymodule.person1["Age"]
# print(a)

# Re-naming a Module
# import mymodule as mx
# a=mx.person1["Age"]
# print(a)


# Built-in Modules
# There are several built-in modules in Python, which you can import whenever you like.

# import platform
# x=platform.system()
# print(x)

# import platform
# x=dir(platform)
# print(x)

# NOTE:The dir() function can be used on all modules, also the ones you create yourself.




from mymodule import person1
print(person1["Age"])

# NOTE: When importing using the from keyword, do not use the module name when referring to elements in the module. Example: person1["age"], not mymodule.person1["age"]

