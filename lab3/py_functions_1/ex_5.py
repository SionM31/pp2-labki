# Write a function that accepts string from user and print all permutations of that string.
from itertools import permutations

def perm(string):
    [print(''.join(i)) for i in list(permutations(string))]

string = str(input("Input a string: "))
print("There is all permutations below:")
perm(string)