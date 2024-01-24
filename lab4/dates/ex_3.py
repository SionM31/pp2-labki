# Write a Python program to drop microseconds from datetime.

import datetime


x = datetime.datetime
print(x.now().replace(microsecond=0))