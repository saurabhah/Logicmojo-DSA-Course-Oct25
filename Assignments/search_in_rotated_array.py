"""
Given an array of distinct elements, which is formed from some places rotation of a sorted array, find if a given element is present in the array or not.
Note: Try to do it in O(logn) runtime complexity
"""


nums = [4,5,6,7,0,1,2] #3,
target = 0
def solution(nums,target):
    
    l = 0
    r = len(nums)-1
    while l <= r:
        mid = (l+r)//2
        print(mid)
        if nums[mid] == target:
            return mid
        
        if nums[l] < nums[mid]:#sorted left part
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid
        else:
            if nums[mid] >= target <= nums[r]:
                l = mid + 1
    
    return -1


print(solution(nums,target))