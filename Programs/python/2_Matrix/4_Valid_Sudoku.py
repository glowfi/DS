# https://leetcode.com/problems/valid-sudoku, Medium, HashMap / Set / Row-Col-Box Tracking

# Question
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.


# Example 1:
# Input: board =
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

# Example 2:
# Input: board =
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the
# 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

# Constraints:
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.

# Brute
# T.C. - O(m*n)+O(m*n)+O(m*n)
# S.C  - O(m*n)+O(m*n)+O(m*n)

# Intuition
# Validate all rows,cols and 3x3 grid based
# on the given condition

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m, n = len(board), len(board[0])

        # Validate all rows
        for i in range(m):
            visited = set()
            for j in range(n):
                if board[i][j] == ".":
                    continue
                curr_num = int(board[i][j])
                if curr_num < 1 or curr_num > 9:
                    return False
                if curr_num in visited:
                    return False
                visited.add(curr_num)

        # Validate all cols
        for j in range(n):
            visited = set()
            for i in range(m):
                if board[i][j] == ".":
                    continue
                curr_num = int(board[i][j])
                if curr_num < 1 or curr_num > 9:
                    return False
                if curr_num in visited:
                    return False
                visited.add(curr_num)

        # Validate all 9 3x3 matrix
        for br in range(0, 9, 3):
            for bc in range(0, 9, 3):
                visited = set()
                for i in range(br, br + 3):
                    for j in range(bc, bc + 3):
                        if board[i][j] == ".":
                            continue
                        curr_num = int(board[i][j])
                        if curr_num < 1 or curr_num > 9:
                            return False
                        if curr_num in visited:
                            return False
                        visited.add(curr_num)

        return True


# Optimal
# T.C. -
# S.C  -

# Intuition

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        pass
