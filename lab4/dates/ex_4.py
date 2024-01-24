# Write a Python program to calculate two date difference in seconds.

import datetime


x = datetime.datetime.now()
dx = datetime.datetime.now() - datetime.timedelta(hours=1)

print((x - dx).total_seconds())