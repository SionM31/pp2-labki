# Write a Python program to write a list to a file.
file_name = "something2.txt"
some_list = ['data', str(2), str(3)]

f = open(file_name, "a")
for i in some_list:
    f.write(str(i) + ' ')
f.close()