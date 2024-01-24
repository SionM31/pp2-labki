# Write a Python program to calculate the area of regular polygon.
# Input number of sides: 4
# Input the length of a side: 25
# The area of the polygon is: 625


import math
import ex_1

def polygon_area(n, l):
    p = n * l # perimeter
    a = l / (2 * math.tan(ex_1.converter(180 / n))) # tipa height koroche apothem
    return (p * a) / 2

n, l = 4, 25
print(f'The area of the polygon is: {polygon_area(n, l)}')