def nextPermutation(nums):
    n = len(nums)
    
    # 1. Find pivot
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    
    if i >= 0:
        # 2. Find element just larger than nums[i]
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        
        # 3. Swap
        nums[i], nums[j] = nums[j], nums[i]
    
    # 4. Reverse the tail
    nums[i + 1:] = reversed(nums[i + 1:])