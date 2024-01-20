# Create a python file and import some of the functions from the above 13 tasks and try to use them.

from ex_1 import convert
from ex_4 import filter

print(convert(123)) # grams

l = list([0, 1, 2, 3, 4, 5, 6, 7, -2]) # exam_4
print(*l)
l = filter(l)
print(*l)