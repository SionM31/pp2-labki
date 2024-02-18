# Write a Python program that matches a string that
# has an 'a' followed by two to three 'b'.

import re
from row import txt

x = re.search("a(b{2}b?)", txt)

print(x)