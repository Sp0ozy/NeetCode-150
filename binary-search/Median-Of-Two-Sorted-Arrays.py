"""
Median of Two Sorted Arrays
https://neetcode.io/problems/median-of-two-sorted-arrays

Time:  O(log(min(m, n)))
Space: O(1)
"""

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            a, b = nums2, nums1
        else:
            a, b = nums1, nums2

        m, n = len(a), len(b)

        half = (m + n + 1) // 2

        l, r = 0, m
        while l <= r:
            i = (l + r) // 2
            j = half - i

            left1 = a[i-1] if i > 0 else float('-inf')
            right1 = a[i] if i < m else float('inf')
            left2 = b[j-1] if j > 0 else float('-inf')
            right2 = b[j] if j < n else float('inf')

            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    return max(left1, left2)
            elif left1 > right2:
                r = i - 1
            else:
                l = i + 1
