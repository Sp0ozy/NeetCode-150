"""
Evaluate Reverse Polish Notation
https://neetcode.io/problems/evaluate-reverse-polish-notation

Time:  O(n)
Space: O(n)
"""

from operator import add, sub, mul
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {"+": add, "-": sub, "*": mul, "/": lambda a, b: int(a / b)}

        for t in tokens:
            if t in ops:
                b = stack.pop()
                a = stack.pop()
                stack.append(ops[t](a, b))
            else:
                stack.append(int(t))
        return stack.pop()
