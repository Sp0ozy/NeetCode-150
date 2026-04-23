"""
Group Anagrams
https://neetcode.io/problems/anagram-groups

Time:  O(n * k)
Space: O(n * k)
"""
from collections import defaultdict
from typing import List


class Solution:
    # only works with lowercase characters
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         output = []
#         existing_anagrams = {}
#         for _, x in enumerate(strs):
#             srtd = ''.join(sorted(x))
#             if srtd in existing_anagrams:
#                 output[existing_anagrams[srtd]].append(x)
#             else:
#                 output.append([x])
#                 existing_anagrams[srtd] = len(output) - 1
#         return output
