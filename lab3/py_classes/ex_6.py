"""
 Write a program which can filter prime numbers in a list by using filter function.

 Note: Use lambda to define anonymous functions.
"""

def filter(listik):
    x = lambda num: num > 1 and all([(num % i != 0) for i in range(2, int(num ** 0.5) + 1)])

    i = 0
    while i < len(listik):
        if x(listik[i]) == 0:
            listik.pop(i)
        else:
            i += 1
    
    return listik


l = list([0, 1, 2, 3, 4, 5, 6, 7, -2])
print(*l)
l = filter(l)
print(*l)