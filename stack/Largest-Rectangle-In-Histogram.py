"""
Largest Rectangle in Histogram
https://neetcode.io/problems/largest-rectangle-in-histogram

Time:  O(n)
Space: O(n)
"""

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        best = 0
        stack = []
        heights.append(0)

        for i in range(len(heights)):
            start = i
            while stack and heights[i] <= stack[-1][1]:
                idx, height = stack.pop()
                best = max(best, height * (i - idx))
                start = idx
            stack.append((start, heights[i]))

        return best
