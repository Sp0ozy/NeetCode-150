"""
Time Based Key-Value Store
https://neetcode.io/problems/time-based-key-value-store

Time:  set O(1), get O(log n)
Space: O(n)
"""

from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.elements = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.elements[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.elements[key]
        res = ""
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid][0] <= timestamp:
                res = arr[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return res
