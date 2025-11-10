"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

"""
nums = [1,2,3,4,5,6,7]
k = 3

# def rotate(nums,k):
#     n = len(nums)
#     k%=n
#     for _ in range(k):
#         last = nums[-1]
#         for i in range(n-1,0,-1):
#             nums[i] = nums[i-1]
#         nums[0] = last
    
#     return nums
# # print(rotate(nums,k))

# def rotate2(nums,k):
#     n = len(nums)
#     k%=n

#     res = [0]*n
#     print(res)
#     j = 0
#     for i in range(n):
#         print((i + k) % n)
#         res[(i + k) % n] = nums[i]

#     return res

# print(rotate2(nums,k))

def rotate(nums,k):
    n = len(nums)
    
    def reverse(left,right):
        while left < right:
            nums[left],nums[right] = nums[right],nums[left]
            right-=1
            left+=1

    reverse(0,n-1)
    reverse(0,k-1)
    reverse(k,n-1)
    print(nums)

print(rotate(nums,k))