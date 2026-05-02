"""
Container With Most Water
https://neetcode.io/problems/max-water-container

Time:  O(n)
Space: O(n)
"""
from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0 , len(heights)-1
        max_amt = 0
        while l<r:
            cur_amt = (r - l) * min(heights[l], heights[r])
            max_amt = max(max_amt,cur_amt)
            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1
        return max_amt