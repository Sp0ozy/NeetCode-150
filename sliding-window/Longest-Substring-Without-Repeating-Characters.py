"""
Longest Substring Without Repeating Characters
https://neetcode.io/problems/longest-substring-without-duplicates

Time:  O(n)
Space: O(1)
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        values = {}
        start = 0
        max_len = 0
        for finish, ch in enumerate(s):
            if ch in values and values[ch] >= start:
                start = values[ch] + 1
            values[ch] = finish
            max_len = max(max_len, finish - start + 1)
        return max_len
