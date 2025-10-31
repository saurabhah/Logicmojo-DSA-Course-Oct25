
"""
Time Complexity:

Worst & Average: $ O(n^2) $
Best (already sorted): $ O(n) $ with optimization


Space Complexity: $ O(1) $ – in-place sorting
Stable: Yes (equal elements keep original order)
Use Case: Educational purposes; not efficient for large datasets
"""

def bubble_sort(arr):
    
    print(arr)
    for i in range(len(arr)):
        swapped = False
        print(arr)
        for j in range(0,len(arr)-i-1):
            print(j)
            exit(0)
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        #this steps make it effiecient 
        if not swapped:
            break

arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(arr))