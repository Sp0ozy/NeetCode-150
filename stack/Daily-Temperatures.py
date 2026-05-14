"""
Daily Temperatures
https://neetcode.io/problems/daily-temperatures

Time:  O(n)
Space: O(n)
"""

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                j = stack.pop()
                output[j] = i - j
            stack.append(i)
        return output
