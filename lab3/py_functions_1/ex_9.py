# Write a function that computes the volume of a sphere given its radius.
from math import pi

def volume(r):
    return (4 / 3) * pi * (r ** 3)


r = int(input("Input a radius of a sphere: "))
print(f'{volume(r)} is a volume of sphere with radius {r}')