"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
"""
nums = [3,0,1]
def missingNumber(nums):
    num_set = set(nums)

    for idx , num in enumerate(num_set):
        if idx!= num:
            return idx
    
    return len(nums)

print(missingNumber(nums))