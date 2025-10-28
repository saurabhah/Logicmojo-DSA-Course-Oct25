"""
Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.

Input Format

Integer N.
Integer Array of size N
"""

arr = [0,1,2,1,2]

def sort_an_array(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        print(arr,arr[mid])
        if arr[mid] == 0:
            arr[low],arr[mid] = arr[mid] ,arr[low]
            mid+=1
            low+=1
        elif arr[mid] == 1:
            mid+=1
        else:
            arr[mid],arr[high] = arr[high],arr[mid]
            high-=1
    
    return arr



print(sort_an_array(arr))