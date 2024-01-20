# Write a function that accepts string from user, return a sentence with the words reversed.

# We are ready -> ready are We

def reverse(string):
    string_list = list(map(str, string.split()))

    return ' '.join(string_list[::-1])

string = input("Input a string: ")
print(f'Reversed: {reverse(string)}')