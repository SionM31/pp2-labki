# Write a Python program to convert degree to radian.
# Input degree: 15
# Output radian: 0.261904

import math

def converter(degrees):
    radians = degrees * math.pi / 180
    return radians


degrees = 15
print(f'60 degrees in radians is: {converter(degrees)}')