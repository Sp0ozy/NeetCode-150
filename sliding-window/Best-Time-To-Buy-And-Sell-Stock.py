"""
Best Time to Buy and Sell Stock
https://neetcode.io/problems/buy-and-sell-crypto

Time:  O(n)
Space: O(1)
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_min = prices[0]
        best_profit = 0
        for p in prices:
            current_min = min(current_min, p)
            best_profit = max(best_profit, p - current_min)
        return best_profit
