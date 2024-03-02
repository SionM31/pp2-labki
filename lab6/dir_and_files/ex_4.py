# Write a Python program to count the number of lines in a text file.
import os 

direct = os.getcwd()
path = os.path.join(direct, "something.txt")

f, counter = open(path, "r"), 0
for _ in f:
    counter += 1

print(counter)