# Write a Python program to replace all occurrences of space,
# comma, or dot with a colon.

import re
from row import txt

x = re.sub("[.,\s]", ":", txt)
print(x)