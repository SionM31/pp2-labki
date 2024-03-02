# Write a Python program to copy the contents of a file to another file
file_name, to_copy, text = "something.txt", "something2.txt", ""

f = open(file_name, "r")
text = f.read()
f.close()

f = open(to_copy, "w")
f.write(text)
f.close()