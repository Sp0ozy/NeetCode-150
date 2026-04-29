"""
Valid-Palindrome
https://neetcode.io/problems/is-palindrome

Time:  O(n)
Space: O(1)
"""
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        ls = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        l,r = 0, len(ls)-1 
        while l<r:
            if not ls[l] == ls[r]:
                return False
            l+=1
            r+=-1
        return True
