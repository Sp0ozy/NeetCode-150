"""
Trapping Rain Water
https://neetcode.io/problems/trapping-rain-water

Time:  O(n)
Space: O(n)
"""

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        max_pre = [0]*len(height)
        max_left = 0
        for i in range(1,len(height)):
            max_left = max(max_left, height[i-1])   
            max_pre[i] = max_left

        max_suf = [0]*len(height)
        max_right = 0
        for i in range(len(height)-2,-1,-1):
            max_right = max(max_right, height[i+1])   
            max_suf[i] = max_right
        
        total_area = 0
        for i in range(1, len(height)-1):
            total_area += max(min(max_pre[i],max_suf[i]) - height[i], 0 )
        
        return total_area