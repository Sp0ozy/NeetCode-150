"""
Is Anagram
https://neetcode.io/problems/is-anagram

Time:  O(n+m) 
Space: O(n+m)
"""
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)
        return Counter(s) == Counter(t)
