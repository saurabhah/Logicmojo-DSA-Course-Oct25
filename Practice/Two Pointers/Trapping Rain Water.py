height = [0,1,0,2,1,0,1,3,2,1,2,1]




def solution(height):
    left = 0 
    right = len(height)-1
    water_level = 0
    right_max,left_max = 0,0

    while left < right:
        if height[left] <= height[right]:
            left_max = max(left_max,height[left])
            water_level += left_max - height[left]
            left+=1
        else:
            right_max = max(right_max,height[right])
            water_level += right_max - height[right]
            right-=1
    
    return water_level

