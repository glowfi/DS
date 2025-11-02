# https://leetcode.com/problems/game-of-life, Medium, Simulation / In-place State Encoding

# Question
# According to Wikipedia's article: "The Game of Life, also known simply as Life,
# is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
# The board is made up of an m x n grid of cells, where each cell has an initial state:
# live (represented by a 1) or dead (represented by a 0).
# Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

# Any live cell with fewer than two live neighbors dies as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# The next state of the board is determined by applying the above rules simultaneously to every cell
# in the current state of the m x n grid board. In this process, births and deaths occur simultaneously.

# Given the current state of the board, update the board to reflect its next state.
# Note that you do not need to return anything.

# Example 1:
# Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

# Example 2:
# Input: board = [[1,1],[1,0]]
# Output: [[1,1],[1,1]]

# Brute
# T.C. - O(m*n*8)
# S.C  - O(m*n)

# Intuition
# For each cell determine neighbour count and
# make it live or die based on the the conditions
# given

from typing import List


class Solution:
    def neightbourCount(self, board: List[List[int]], curr_pos: tuple[int, int]) -> int:
        m, n = len(board), len(board[0])
        dirs = [(0, 1), (1, 0), (-1, -1), (1, 1), (0, -1), (-1, 0), (1, -1), (-1, 1)]
        x, y = curr_pos
        c = 0

        for dx, dy in dirs:
            pos_x = x + dx
            pos_y = y + dy

            if pos_x < 0 or pos_x >= m:
                continue

            if pos_y < 0 or pos_y >= n:
                continue

            if board[pos_x][pos_y] == 1:
                c += 1

        return c

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        res = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                neightbourCount = self.neightbourCount(
                    board,
                    (
                        i,
                        j,
                    ),
                )
                if board[i][j] == 1:
                    if neightbourCount == 2 or neightbourCount == 3:
                        res[i][j] = 1
                    elif neightbourCount < 2:
                        res[i][j] = 0
                    elif neightbourCount > 3:
                        res[i][j] = 0
                else:
                    if neightbourCount == 3:
                        res[i][j] = 1

        board[:] = res


# Optimal
# T.C. - O(m*n)+O(m*n)
# S.C  - O(1)

# Intuition
# We need to somehow store the previous state of our matrix
# For each cell ge the neightbour count
# What we can do is mark the cell that will become living state to dead state with -2
# and cell that will become dead state to living with 2.
# At last conver thr -2 to 0 and 2 to 1

from typing import List


class Solution:
    def neightbourCount(self, board: List[List[int]], curr_pos: tuple[int, int]) -> int:
        m, n = len(board), len(board[0])
        dirs = [(0, 1), (1, 0), (-1, -1), (1, 1), (0, -1), (-1, 0), (1, -1), (-1, 1)]
        x, y = curr_pos
        c = 0

        for dx, dy in dirs:
            pos_x = x + dx
            pos_y = y + dy

            if pos_x < 0 or pos_x >= m:
                continue

            if pos_y < 0 or pos_y >= n:
                continue

            if board[pos_x][pos_y] in [1, -2]:
                c += 1

        return c

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                neightbourCount = self.neightbourCount(
                    board,
                    (
                        i,
                        j,
                    ),
                )
                if board[i][j] == 1:
                    if neightbourCount < 2:
                        board[i][j] = -2
                    elif neightbourCount > 3:
                        board[i][j] = -2
                else:
                    if neightbourCount == 3:
                        board[i][j] = 2

        for i in range(m):
            for j in range(n):
                if board[i][j] == -2:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1
