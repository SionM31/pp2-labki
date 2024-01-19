"""
    Tuple
    Tuples are used to store multiple items in a single variable.

    Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

    A tuple is a collection which is ordered and unchangeable.

    Tuples are written with round brackets.
"""

#Create a Tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Tuple Items
# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.


# When we say that tuples are ordered, 
# it means that the items have a defined order,
# and that order will not change.


# Tuples are unchangeable,
# meaning that we cannot change,
# add or remove items after the tuple has been created.


# Since tuples are indexed, they can have items with the same value:
# Tuples allow duplicate values:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)


# To determine how many items a tuple has, use the len() function:
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))


# To create a tuple with only one item,
# you have to add a comma after the item,
# otherwise Python will not recognize it as a tuple.
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))


# Tuple items can be of any data type:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

# A tuple can contain different data types:
tuple1 = ("abc", 34, True, 40, "male")

"""
 type()

 From Python's perspective, tuples are defined as objects with the data type 'tuple':
 
 <class 'tuple'>
"""


# It is also possible to use the tuple() constructor to make a tuple.
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)