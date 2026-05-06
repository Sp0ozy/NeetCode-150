"""
3Sum
https://neetcode.io/problems/three-integer-sum

Time:  O(n^2)
Space: O(n)
"""
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        for i,x in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l,r = i+1,len(nums)-1
            while l<r:
                curSum = nums[l] + nums[r]
                if curSum < -x:
                    l+=1
                elif curSum > -x:
                    r-=1
                else:
                    output.append([nums[l], x, nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
        return output