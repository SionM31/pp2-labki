# Write a Python program to delete file by specified path.
# Before deleting check for access and whether a given path exists or not.
import os

def checker(path):
    if not os.access(path, os.F_OK):
        return False

    if not os.access(path, os.X_OK):
        return False
    
    return True

direct = os.getcwd()
path = os.path.join(direct, "something3.txt")

if(checker(path)):
    os.remove(path)
else:
    print("Create a file named something3.txt pls")