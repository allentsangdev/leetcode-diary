from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # check row
        for row in board:
            # using a set here since appending an element to a set is O(1)
            rowCheck = set()
            for cell in row: 
                if cell == '.':
                    continue
                if cell in rowCheck:
                    return False
                elif cell not in rowCheck:
                    rowCheck.add(cell)
        
        # check col
        colCheck = defaultdict(set)
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue
                if board[row][col] not in colCheck[col]:
                    colCheck[col].add(board[row][col])
                elif board[row][col] in colCheck[col]:
                    return False
                    
        # check 3 * 3 grid
        squareCheck = defaultdict(set)
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue
                if board[row][col] not in squareCheck[(row//3, col//3)]:
                    squareCheck[(row//3, col//3)].add(board[row][col])
                else:
                    return False
                    
        return True