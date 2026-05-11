"""
Minimum Stack
https://neetcode.io/problems/minimum-stack

Time:  O(1)
Space: O(n)
"""

class MinStack:

    def __init__(self):
        self._stack = []
        self._minstack = []

    def push(self, val: int) -> None:
        self._stack.append(val)
        if not self._minstack or self._minstack[-1] >= val:
            self._minstack.append(val)

    def pop(self) -> None:
        if self._stack[-1] == self._minstack[-1]:
            self._minstack.pop()
        self._stack.pop()

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._minstack[-1]
