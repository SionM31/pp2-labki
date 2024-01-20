"""
 Define a functino histogram() that takes a list of integers and prints a histogram to the screen.
 
 For example, histogram([4, 9, 7]) should print the following:
"""

def histogram(nums):
    [print('*' * nums[i]) for i in range(len(nums))]


nums = list(map(int, input("Vvedite chisla: ").split()))
histogram(nums)