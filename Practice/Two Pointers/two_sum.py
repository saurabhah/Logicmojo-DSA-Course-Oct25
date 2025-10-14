nums = [3,2,4]
target = 6


def solution1(nums,target):
    """
    Space complexity O(n)
    Time complexity O(n)
    """
    hash_map = {}
    for idx,num in enumerate(nums):
        if target - num in hash_map:
            return [hash_map[target-num],idx]
        
        hash_map[num] = idx



print(solution1(nums,target))