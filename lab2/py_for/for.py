"""
A for loop is used for iterating over a sequence
(that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages,
and works more like an iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, 
once for each item in a list, tuple, set etc.
"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


# Even strings are iterable objects, they contain a sequence of characters:
for x in "banana":
  print(x)


# With the break statement we can stop the loop before it has looped through all the items:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

# Exit the loop when x is "banana", but this time the break comes before the print:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)


# With the continue statement we can stop the current iteration of the loop,
# and continue with the next:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


# To loop through a set of code a specified number of times, we can use the range() function,
for x in range(6):
  print(x)

# Using the start parameter:
for x in range(2, 6):
  print(x)

# Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):
  print(x)


# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
for x in range(6):
  print(x)
else:
  print("Finally finished!")

# Break the loop when x is 3, and see what happens with the else block:
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")


# Print each adjective for every fruit:
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


# for loops cannot be empty,
# but if you for some reason have a for loop with no content,
# put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
  pass