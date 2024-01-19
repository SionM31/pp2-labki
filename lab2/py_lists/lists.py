"""
    List
    Lists are used to store multiple items in a single variable.
    
    Lists are one of 4 built-in data types in Python used to store collections of data,

    the other 3 are Tuple, Set, and Dictionary, 
    
    all with different qualities and usage.
    
    Lists are created using square brackets:
"""
thislist = ["apple", "banana", "cherry"]
print(thislist)


"""
    List Items
    List items are ordered, changeable, and allow duplicate values.

    List items are indexed, the first item has index [0], the second item has index [1] etc.
"""


"""
    Changeable
    The list is changeable, meaning that we can change, 
    
    add, and remove items in a list after it has been created.
"""


"""
    Allow Duplicates
    Since lists are indexed, lists can have items with the same value:

    Lists allow duplicate values:
"""
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)


# To determine how many items a list has, use the len() function:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))