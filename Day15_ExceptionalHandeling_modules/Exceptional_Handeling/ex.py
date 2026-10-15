'''
try: The try block lets you test a block of code for errors.
except: The except block lets you handle the error.
else: The else block lets you execute code when there is no error
finally: The finally block lets you execute code, regardless of the result of the try- and except blocks.
Raise: To throw (or raise) an exception, use the raise keyword.

Exception Handling: When an error occurs, or exception as 
we call it, Python will normally stop and generate an error message.
These exceptions can be handled using the try statement:

Error Types:
Syntax error
ValueError
OutOfRange
ZeroDivisionError
NameError

'''

# try:
#     print(x)
# except:
#     print("An exception occured")
# Since the try block raises an error, the except block will be executed.

# ----------------------------------------------------
# Many Exceptions
# try:
#     print(x)
# except NameError:
#     print("Variable x is not defined")
# except:
#     print("Something else went wrong")

# try:
#     print(x)
# except ValueError:
#     print("Variable x is not defined")
# except:
#     print("Something else went wrong")

# -----------------------------------------------------------
# Else
# In this example, the try block does not generate any error:

# try:
#     print("Hello")
# except:
#     print("Something went wrong")
# else:
#     print("Nothing went wrong")

# ----------------------------------------------------------------
# Finally(The finally block, if specified, will be executed regardless if the try block raises an error or not.)
# try:
#     print(x)
# except:
#     print("Something went wrong")
# finally:
#     print("The 'Try except' is finished ")


# -------------------------------------------------------------
# Raise
# x=-1
# if x < 0:
#     raise Exception("Sorry, no number below zero")

# x='hello'

# if not type(x) is int:
#     raise Exception("Only integer are allowed")