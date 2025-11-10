"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
"""

nums = [100,4,200,1,3,2]


def solution(nums):
    num_set = set(nums)
    longest = 0
    for num in num_set:
        #start of sequence
        if num - 1 not in num_set:
            current_num = num
            steak = 1

            while current_num + 1 in num_set:
                current_num += 1
                steak+=1
            
            longest = max(longest,steak)



    
    return longest

        


print(solution(nums))