"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
"""




class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u']
        s = list(s)
        left,right = 0, len(s) -1

        while left < right:
            if s[left].lower() in vowels and s[right].lower() in vowels:
                s[left],s[right] = s[right],s[left]
                left+=1
                right-=1
            elif s[left].lower() not in vowels:
                left+=1
            elif s[right].lower() not in vowels:
                right-=1
        
        return ''.join(s)