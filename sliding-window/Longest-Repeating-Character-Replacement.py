"""
Longest Repeating Character Replacement
https://neetcode.io/problems/longest-repeating-substring-with-replacement

Time:  O(n)
Space: O(1)
"""

from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l = 0
        max_count = 0
        result = 0
        for r in range(len(s)):
            count[s[r]] += 1
            max_count = max(max_count, count[s[r]])
            win_len = r - l + 1
            if win_len - max_count > k:
                count[s[l]] -= 1
                l += 1
            result = max(result, r - l + 1)
        return result
