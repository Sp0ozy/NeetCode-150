"""
Koko Eating Bananas
https://neetcode.io/problems/eating-bananas

Time:  O(n log m)
Space: O(1)
"""

import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower, upper = 1, max(piles)
        best = upper
        while lower <= upper:
            k = (lower + upper) // 2
            time = 0

            for p in piles:
                time += math.ceil(p / k)

            if time > h:
                lower = k + 1
            else:
                upper = k - 1
                best = min(best, k)
        return best
