# Write a Python program to check for access to a specified path.
# Test the existence, readability, writability and executability of the specified path
import os

def checker(path):
    if os.access(path, os.F_OK):
        print("The path exists")
    else:
        print("The path does not exists")

    if os.access(path, os.R_OK):
        print("The path is readable")
    else:
        print("The path is not readable")
    
    if os.access(path, os.W_OK):
        print("The path is writable")
    else:
        print("The path is not writable")
    
    if os.access(path, os.X_OK):
        print("The path is executable")
    else:
        print("The path is not executable")


direct = os.getcwd()
pathik = os.path.join(direct, "something.txt")

print(pathik)
checker(pathik)