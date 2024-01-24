# Write a Python program to print yesterday, today, tomorrow.

import datetime


x = datetime.datetime.now()
print(f'Yesterday was {x.strftime("%A")}')
print(f'Today is {(x - datetime.timedelta(days=1)).strftime("%A")}')
print(f'Tomorrow will be {(x + datetime.timedelta(days=1)).strftime("%A")}')