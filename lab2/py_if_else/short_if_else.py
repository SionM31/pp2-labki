# If you have only one statement to execute, one for if,
# and one for else, you can put it all on the same line:
a = 2
b = 330
print("A") if a > b else print("B")

# You can also have multiple else statements on the same line:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")