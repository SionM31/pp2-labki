"""
 Write a Python function that checks whether a word or phrase is palindrome or not.

 Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam
"""

def is_palindrome(string):
    return string == string[::-1]

string = str(input())
print(is_palindrome(string))