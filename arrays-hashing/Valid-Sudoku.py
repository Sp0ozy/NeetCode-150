"""
Valid Sudoku
https://neetcode.io/problems/valid-sudoku

Time:  -
Space: -
"""
from typing import List
from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows = defaultdict(list)
        # cols = defaultdict(list)
        # boxes = defaultdict(list)
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                element = board[r][c]
                if element == '.':
                    continue
                # if element in rows[r] or element in cols[c] or element in boxes[(r//3)*10+(c//3)]:
                if element in rows[r] or element in cols[c] or element in boxes[(r//3)*3+(c//3)]:
                    return False
                # rows[r].append(element)
                # cols[c].append(element)
                # boxes[(r//3)*10+(c//3)].append(element)
                rows[r].add(element)
                cols[c].add(element)
                boxes[(r//3)*3+(c//3)].add(element)
        return True
