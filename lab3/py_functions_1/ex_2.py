"""
 Read in a Fahrenheit temperature.
 
 Calculate and display the equivalent centigrade temperature.
 
 The following formula is used for the conversion: C = (5 / 9) * (F - 32)
"""

def convert(F):
    C = (5 / 9) * (F - 32)
    return C

F = int(input("Input degree in Fahrenheit"))
print(f'Degree in Celsium: {convert(F)}')