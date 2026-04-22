"""
Two Sum
https://neetcode.io/problems/two-integer-sum

Time:  O(n)
Space: O(n)
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i, v in enumerate(nums):
            tmp = target - v
            if tmp in indices:
                return [indices.get(tmp), i]
            indices.update({v: i})
        return []
