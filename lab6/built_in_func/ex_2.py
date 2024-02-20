# Write a Python program with builtin function that accepts a string
# and calculate the number of upper case letters and lower case letters

def calculate(s):
    counter_up, counter_down = 0, 0
    for i in s:
        if i.isupper():
            counter_up += 1
        elif i.islower():
            counter_down += 1
    
    print(f"lower case letters: {counter_down}")
    print(f"upper case letters: {counter_up}")


calculate("AaBbCcDD")