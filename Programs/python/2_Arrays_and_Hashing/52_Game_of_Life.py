# https://leetcode.com/problems/game-of-life , Medium

# Question
# According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician
# John Horton Conway in 1970."

# The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0).
# Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

# Any live cell with fewer than two live neighbors dies as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of
# the m x n grid board. In this process, births and deaths occur simultaneously.

# Given the current state of the board, update the board to reflect its next state.

# Note that you do not need to return anything.

# Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
# Example 2:


# Input: board = [[1,1],[1,0]]
# Output: [[1,1],[1,1]]


# Constraints:

# m == board.length
# n == board[i].length
# 1 <= m, n <= 25
# board[i][j] is 0 or 1.

# Brute
# T.C. - O(M*N*8)
# S.C  - O(M*N)

# Intuition
# Live cell with less than 2 live neighbors die
# Live cell with more than 2 or 3 live neighbors live
# Live cell with more than 3 live die
# Dead cell ressurects with exactly 3 live neighbors


from typing import List


class Solution:
    def get_live_neighbour_count(self, x: int, y: int, board: List[List[int]]):
        dirs = [(1, 0), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1), (0, -1), (-1, 0)]

        live_neighbor_count = 0
        for dx, dy in dirs:
            if 0 <= x + dx < len(board) and 0 <= y + dy < len(board[0]):
                if board[x + dx][y + dy] == 1:
                    live_neighbor_count += 1

        return live_neighbor_count

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        ans = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[0])):
                live_neighbor_count = self.get_live_neighbour_count(i, j, board)
                if board[i][j] == 1:
                    if live_neighbor_count > 3 or live_neighbor_count < 2:
                        ans[i][j] = 0
                    else:
                        ans[i][j] = 1
                else:
                    if live_neighbor_count == 3:
                        ans[i][j] = 1

        board[::] = ans


# Optimal
# T.C. - O(M*N*8)+O(M*N) ~ O(M*N)
# S.C  - O(1)

# Intuition
# we try to preserve the original values of each state
# mark the cell that was alive but will die as -2
# mark the cell that was dead but ressurects with 2

from typing import List


class Solution:
    def get_live_neighbour_count(self, x: int, y: int, board: List[List[int]]):
        dirs = [(1, 0), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1), (0, -1), (-1, 0)]

        live_neighbor_count = 0
        for dx, dy in dirs:
            if 0 <= x + dx < len(board) and 0 <= y + dy < len(board[0]):
                if board[x + dx][y + dy] in [1, -2]:
                    live_neighbor_count += 1

        return live_neighbor_count

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        for i in range(len(board)):
            for j in range(len(board[0])):
                live_neighbor_count = self.get_live_neighbour_count(i, j, board)
                if board[i][j] == 1:
                    if live_neighbor_count > 3 or live_neighbor_count < 2:
                        board[i][j] = -2
                else:
                    if live_neighbor_count == 3:
                        board[i][j] = 2

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == -2:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1
