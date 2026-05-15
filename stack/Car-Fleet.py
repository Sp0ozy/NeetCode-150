"""
Car Fleet
https://neetcode.io/problems/car-fleet

Time:  O(n log n)
Space: O(n)
"""

from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars.sort(key=lambda x: x[0], reverse=True)
        fleets = [(target - cars[0][0]) / cars[0][1]]
        for c in cars[1:]:
            if fleets[-1] < (target - c[0]) / c[1]:
                fleets.append((target - c[0]) / c[1])
        return len(fleets)
