"""
Write a function that takes in a list of integers and returns True if it contains 007 in order

def spy_game(nums):
    pass

spy_game([1,2,4,0,0,7,5]) --> True
spy_game([1,0,2,4,0,5,7]) --> True
spy_game([1,7,2,0,4,5,0]) --> False
"""

def spy_game(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 0:
            for j in range(i + 1, len(nums) - 1):
                if nums[j] == 0:
                    for h in range(j + 1, len(nums)):
                        if nums[h] == 7:
                            return True
    
    return False


nums = list(map(int, input("Enter some integers: ").split()))
print(spy_game(nums))