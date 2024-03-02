# Write a Python program to test whether a given path exists or not.
# If the path exist find the filename and directory portion of the given path.
import os

direct = os.getcwd()
path = os.path.join(direct, "something.txt")

if not os.access(path, os.F_OK):
    print("The path does not exist")
else:
    print(f'Filename is: {os.path.basename(path)}')
    print(f'Directory portion is: {os.path.dirname(path)}')