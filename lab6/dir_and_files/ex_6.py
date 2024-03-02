# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
file_name = 'A'
while file_name != 'Z':
    f = open(f'{file_name}.txt', "a")
    f.close()
    file_name = chr(ord(file_name) + 1)
