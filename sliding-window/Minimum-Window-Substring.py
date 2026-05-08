"""
Minimum Window Substring
https://neetcode.io/problems/minimum-window-with-characters

Time:  O(n)
Space: O(n)
"""

import math
from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        have = defaultdict(int)
        formed = 0
        required = len(need)
        left = 0
        best = (math.inf, 0, 0)

        for right, c in enumerate(s):
            have[c] += 1
            if c in need and have[c] == need[c]:
                formed += 1

            while formed == required:
                if right - left + 1 < best[0]:
                    best = (right - left + 1, left, right)
                have[s[left]] -= 1
                if s[left] in need and have[s[left]] < need[s[left]]:
                    formed -= 1
                left += 1

        return s[best[1]:best[2] + 1] if best[0] < math.inf else ""
