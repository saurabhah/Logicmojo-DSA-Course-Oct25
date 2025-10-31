"""
Time Complexity:

CaseComplexityWorst & Average$ O(n^2) $Best$ O(n^2) $ (no early exit)

Space Complexity: $ O(1) $ – in-place sorting
Stable: No (swaps can change relative order of equal elements)
Use Case: Educational; good when swap cost is high (few swaps)
vs. Bubble Sort: Selection has fewer swaps but more comparisons
"""

def selection_sort(arr):
    print(arr)

    for i in range(len(arr)):
        min_idx = i

        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j 
    
        arr[i],arr[min_idx] = arr[min_idx],arr[i]
    
    return arr

arr = [64, 25, 12, 22, 11, 90, 34]
print(selection_sort(arr))