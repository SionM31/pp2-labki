"""
 Write a Python function that takes a list and returns a new list with unique elements of the first list.

 Note: don't use collection set.
"""

def unique(listik):
    setik = []

    return [setik.append(i) for i in listik if i not in setik]

listik = list(input("Input some several values: ").split())
print(*unique(listik))