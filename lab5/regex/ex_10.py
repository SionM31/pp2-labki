# Write a Python program to convert a given camel case string to snake case.
import re

s = "camelCaseStringExample"
x = re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()
print(x)