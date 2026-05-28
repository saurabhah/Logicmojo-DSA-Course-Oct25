"""Given two strings s and t, return true if t is an anagram of s, and false otherwise."""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!= len(t):
            return False
            
        count = {}

        for letter in s:
            if letter in count:
                count[letter] +=1
            else:
                count[letter] = 1
        
        for letter in t:
            if letter in count:
                count[letter] -=1
            else:
                count[letter] = 1
        # print(count)
        for k,v in count.items():
            # print(k,v)
            if v != 0:
                return False
        
        return True
    
print(Solution().isAnagram(s = "anagram", t = "nagaram"))