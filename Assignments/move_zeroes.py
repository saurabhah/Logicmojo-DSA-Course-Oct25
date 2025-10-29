"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
"""


arr = [1,0,0,0,2,3,4]

def move_func(arr):
    i = 0
    for num in arr:
        if num != 0:
            arr[i] = num
            i+=1

    for j in range(i,len(arr)):
        arr[j] = 0
    
    return arr
    
print(move_func(arr))
