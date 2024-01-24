# Write a Python program to calculate the area of a trapezoid.
# Height: 5
# Base, first value: 5
# Base, second value: 6
# Expected Output: 27.5


def trapezoid_area(a, b, h):
    area = (a + b) * h / 2
    return area

a = 5
b = 6
h = 5
print(trapezoid_area(a, b, h))