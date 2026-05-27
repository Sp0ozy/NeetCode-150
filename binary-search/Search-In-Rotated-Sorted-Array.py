"""
Search in Rotated Sorted Array
https://neetcode.io/problems/find-target-in-rotated-sorted-array

Time:  O(log n)
Space: O(1)
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (r + l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        min_idx = l
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = ((r + l) // 2 + min_idx) % (len(nums))
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = (r + l) // 2 - 1
            else:
                l = (r + l) // 2 + 1

        return -1


# Alternative: single-pass binary search (no separate pivot search)
class SolutionAlt:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (r + l) // 2
            if target == nums[mid]:
                return mid

            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
