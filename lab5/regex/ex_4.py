# Write a Python program to find the sequences of one upper case letter followed by lower case letters.

import re
from row import txt

x = re.findall("[A-Z][a-z]+", txt)
print(x)