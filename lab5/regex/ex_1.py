# Write a Python program that matches a string that has an 'a'
# followed by zero or more 'b''s.

import re
from row import txt

x = re.search("ab*", txt)
print(x)