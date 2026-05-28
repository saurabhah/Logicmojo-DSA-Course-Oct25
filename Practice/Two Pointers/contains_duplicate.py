"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_map  =set()

        for num in nums:
            if num in hash_map:
                return True
            hash_map.add(num)
        
        return False
    
print(Solution().containsDuplicate(nums = [1,2,3,1]))