"""
Two Integer Sum II
https://neetcode.io/problems/two-integer-sum-ii

Time:  O(n)
Space: O(1)
"""
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0 , len(numbers)-1
        while l<r:
            current = numbers[l] + numbers[r]
            if current == target:
                return [l+1,r+1]
            if current > target:
                r-=1
            else:
                l+=1
        return []