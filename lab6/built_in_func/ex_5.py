# Write a Python program with builtin function that returns True if all elements of the tuple are true.
def func(arraychik):
    return all(arraychik)

array1 = [1, 2, 3]
array2 = [1, 0, 2]

print(func(array1))
print(func(array2))