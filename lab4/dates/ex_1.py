# Write a Python program to subtract five days from current date.

import datetime


print(datetime.datetime.now() - datetime.timedelta(days=5))