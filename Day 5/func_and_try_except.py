#This is function and this task we call hello_print function and two number sum.

def hello_print(num1, num2):
    print(num1*num2)
    
hello_print(8,9)

print("================")
#This is task we check data types

my_var = "some text"
my_int = 1

print(type(my_var))
print(type(my_int))

print("================")

#This is task through you can understand how to work global variables

my_string = "Hello World"

def change_strings():
    global my_string
    my_string += " from Roza"

change_strings()
print(my_string)

#This is task try/except about
#name = "Roza"
"""
try:
    print(name)
except:
    print("Name is not defined...")

print("Continue")

"""

