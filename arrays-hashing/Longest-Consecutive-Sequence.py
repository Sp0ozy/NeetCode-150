"""
Longest Consecutive Sequence
https://neetcode.io/problems/longest-consecutive-sequence

Time:  O(n)
Space: O(n)
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        final_len = 0
        for x in numbers:
            if x-1 in numbers:
                continue
            length = 1
            while x+length in numbers:
                length+=1
            final_len = max(final_len, length)

        return final_len
