"""
Top K Frequent Elements
https://neetcode.io/problems/top-k-elements-in-list

Time:  O(n)
Space: O(n)
"""
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)

        res = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         counter = defaultdict(int)
#         for x in nums:
#             counter[x] += 1
#         return [t[0] for t in sorted(counter.items(), key=lambda item: item[1], reverse=True)[:k]]
