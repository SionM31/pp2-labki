# Write a Python program to split a string at uppercase letters.
import re

stringi = "SplitThisStringAtUpperCase"
x = re.findall('[A-Z][^A-Z]*', stringi)
print(x)