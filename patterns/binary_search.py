nums = [1,2,3,4,5,6,7,8]

target = 6
def solution(nums):
    
    start = 0
    end = len(nums)-1

    while start <= end:
        mid = (start + end)//2
        if nums[mid] == target:
            return mid
        if nums[mid] <= target:
            start = mid + 1
        if nums[mid] >= target:
            end = mid -1

    return -1





print(solution(nums))