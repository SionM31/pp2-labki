# A set is a collection which is unordered, unchangeable*, and unindexed.
# Sets are written with curly brackets.
thisset = {"apple", "banana", "cherry"}
print(thisset)

# Sets are unordered, so you cannot be sure in which order the items will appear.


# Set items are unordered, unchangeable, and do not allow duplicate values.

# Unordered means that the items in a set do not have a defined order.

# Set items are unchangeable, meaning that we cannot change the items after the set has been created.

# Duplicate values will be ignored:
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)


# True and 1 is considered the same value:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

# False and 0 is considered the same value:
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)


# To determine how many items a set has, use the len() function.
thisset = {"apple", "banana", "cherry"}
print(len(thisset))


# Set items can be of any data type:
set1 = {"apple", "banana", "cherry"} # string
set2 = {1, 5, 7, 9, 3}               # int
set3 = {True, False, False}          # boolean

set1 = {"abc", 34, True, 40, "male"} # multi-type


# What is the data type of a set?
myset = {"apple", "banana", "cherry"}
print(type(myset))  # <class 'set'>

# It is also possible to use the set() constructor to make a set.
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)