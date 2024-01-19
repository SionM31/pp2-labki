# List comprehension offers a shorter syntax when you want to create 
# a new list based on the values of an existing list.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# With list comprehension you can do all that with only one line of code:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


# The Syntax

# newlist = [expression for item in iterable if condition == True]
# The return value is a new list, leaving the old list unchanged.


# The condition is like a filter that only accepts the items that valuate to True.
newlist = [x for x in fruits if x != "apple"]

# The condition is optional and can be omitted:
newlist = [x for x in fruits]


# The iterable can be any iterable object, like a list, tuple, set etc.
newlist = [x for x in range(10)]

# Accept only numbers lower than 5:
newlist = [x for x in range(10) if x < 5]


# The expression is the current item in the iteration,
# but it is also the outcome, 
# which you can manipulate before it ends up like a list item in the new list:
newlist = [x.upper() for x in fruits]

# You can set the outcome to whatever you like:
newlist = ['hello' for x in fruits]

# The expression can also contain conditions, not like a filter, 
# but as a way to manipulate the outcome:
newlist = [x if x != "banana" else "orange" for x in fruits]