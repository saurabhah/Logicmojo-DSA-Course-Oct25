"""
Docstring for Practice.arrays.product_of_array_except_itself
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements
 of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

A More Efficient Way (No Division):

A common approach to solve this problem is to use two arrays (or lists):

One array stores the product of all the numbers before the current number.

Another array stores the product of all the numbers after the current number.



"""

def productExceptSelf(nums):
    res = []

    prefix = 1
    for i in range(len(nums)):
        res.append(prefix)
        prefix *= nums[i]
    
    postfix = 1

    for i in range(len(nums)-1,-1,-1):
        res[i] *= postfix
        postfix*= nums[i]
    return res


def solution(nums):
    res = [1] * len(nums)
  
    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)-1,0,-1):
            if nums[i] != nums[j]:
               
                product = product*nums[j]
                res[i] = product
                
        
    return res

