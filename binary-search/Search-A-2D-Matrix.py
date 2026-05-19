"""
Search a 2D Matrix
https://neetcode.io/problems/search-2d-matrix

Time:  O(log m + log n)
Space: O(1)
"""

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        mid = 0

        while top <= bottom:
            mid = (top + bottom) // 2
            if matrix[mid][left] <= target and matrix[mid][right] >= target:
                break
            elif matrix[mid][left] > target:
                bottom = mid - 1
            elif matrix[mid][right] < target:
                top = mid + 1

        while left <= right:
            mid2 = (left + right) // 2
            if matrix[mid][mid2] == target:
                return True
            elif matrix[mid][mid2] < target:
                left = mid2 + 1
            else:
                right = mid2 - 1

        return False
