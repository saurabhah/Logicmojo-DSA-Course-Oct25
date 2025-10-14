"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""


def solution(haystack,needle):
    n = len(needle)
    for i in range(len(haystack)):
        if haystack[i:n] == needle:
            return i
        n+=1 

    return -1

    

print(solution(haystack="sadbutsad",needle = "sad"))