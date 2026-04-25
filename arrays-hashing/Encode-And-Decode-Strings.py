"""
Encode and Decode Strings
https://neetcode.io/problems/string-encode-and-decode

Time:  O(n)
Space: O(n)
"""
from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for x in strs:
            output += f"{len(x)}#{x}"
        return output


    def decode(self, s: str) -> List[str]:
        output=[]
        i=0
        while i <len(s):
            j=i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            output.append(s[j+1:j+1+length])
            i=j+1+length
        return output
