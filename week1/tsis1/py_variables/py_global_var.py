#Variables that are created outside of a function 
#(as in all of the examples above) are known as global variables.

#Global variables can be used by everyone, both inside of functions and outside.
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

"""
If you create a variable with the same name inside a function
this variable will be local
and can only be used inside the function.
it will remain as it was
"""

x = "awesome"

def myfunc1():
  x = "fantastic"
  print("Python is " + x)

myfunc1()

print("Python is " + x) 

#or you can use global keyword:
def myfunc2():
  global x
  x = "fantastic"

myfunc2()

print("Python is " + x)

"""
So, if you make x global int myfunc1,
it will change the global variable x inside
the function.
"""