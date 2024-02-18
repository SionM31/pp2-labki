# Write a Python program to insert spaces between words starting with capital letters.
import re

stringi = "ThisIsAStringWithCapitalWords"
x = re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', stringi)

while(x != re.sub(r'(?<=[A-Z])(?=[A-Z][a-z])', ' ', x)):
    x = re.sub(r'(?<=[A-Z])(?=[A-Z][a-z])', ' ', x)

print(x)
