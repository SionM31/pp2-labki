# Write a Python program with builtin function that checks whether a passed string is palindrome or not.
def isPalindrome(s):
    if s == s[::-1]:
        return True
    return False

s1 = "abcda"
s2 = "aboba"

print(isPalindrome(s1))
print(isPalindrome(s2))