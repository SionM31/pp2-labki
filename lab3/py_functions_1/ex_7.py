"""
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def has_33(nums):
    pass

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False
"""

def has_33(nums):
    return bool((''.join(map(str, nums))).find('33') != -1)


nums = list(map(int, input().split()))
print(has_33(nums))