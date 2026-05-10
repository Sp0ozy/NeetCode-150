"""
Valid Parentheses
https://neetcode.io/problems/validate-parentheses

Time:  O(n)
Space: O(n)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}
        for br in s:
            if br not in pairs:
                stack.append(br)
            elif not stack or pairs[br] != stack.pop():
                return False
        return len(stack) == 0
