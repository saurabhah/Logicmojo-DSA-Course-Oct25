"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

"""


strs = ["eat","tea","tan","ate","nat","bat"]

n = len(strs)


for i in strs:
    for j in i:
        print(j,i)
        