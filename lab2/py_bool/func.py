# Functions can Return a Boolean
def myFunction() :
  return True

print(myFunction())


# You can execute code based on the Boolean answer of a function:
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")


# Check if an object is an integer or not:
x = 200
print(isinstance(x, int))