numbers = [-1,0]
target = -1

def solution(numbers,target):
    """
    Space complexity O(n)
    Time complexity O(n)
    """
    l,r = 0, len(numbers)-1

    while l < r:
        two_sum = numbers[l] + numbers[r]
        if two_sum == target:
            return [l+1,r+1]
        
        if two_sum < target:
            l+=1
        
        if two_sum > target:
            r-=1

    return []


print(solution(numbers,target))
