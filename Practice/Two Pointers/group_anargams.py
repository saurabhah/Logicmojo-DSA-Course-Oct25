"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
28-oct-2025
"""


strs = ["eat","tea","tan","ate","nat","bat"]

def groupAnagrams(strs):
    hash_map = {}

    for i in range(len(strs)):
        sorted_word = "".join(sorted(strs[i]))
        if sorted_word not in hash_map:
            hash_map[sorted_word] = [strs[i]]
        else:
            hash_map[sorted_word].append(strs[i])
    
    return list(hash_map.values())

print(groupAnagrams(strs))