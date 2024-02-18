# Write a python program to convert snake case string to camel case string.

import re

def convertor(match):
    return match.group(0)[1].upper()

txt = "snake_case_base_bibibibibi"
x = re.sub(r'_.', convertor, txt)

print(x)