# List items can be of any data type:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]


#A list with strings, integers and boolean values:
list1 = ["abc", 34, True, 40, "male"]


# From Python's perspective, 
# lists are defined as objects with the data type 'list':
mylist = ["apple", "banana", "cherry"]
print(type(mylist)) # <class 'list'>


# It is also possible to use the list() constructor when creating a new list.
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist) # ['apple', 'banana', 'cherry']