# Write a Python program to find sequences
# of lowercase letters joined with a underscore.

import re
from row import txt

x = re.findall("[a-z]+_[a-z]+", txt)

print(x)