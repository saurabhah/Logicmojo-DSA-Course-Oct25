"""
Given an array of distinct elements, which is formed from some places rotation of a sorted array, find if a given element is present in the array or not.
Note: Try to do it in O(logn) runtime complexity
"""


nums = [4,5,6,7,0,1,2] #3,
target = 0
def solution(nums,target):
    
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left+right)//2

        if nums[mid] == target:
            return mid
        
        if nums[left] < nums[mid]:#sorted left part
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] >= target <= nums[right]:#sorted right part
                left = mid + 1
            else:
                right = mid - 1
    
    return -1


print(solution(nums,target))