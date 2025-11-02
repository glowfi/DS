# https://leetcode.com/problems/spiral-matrix, Medium, Simulation / Direction Vectors

# Question
# Given an m x n matrix, return all elements of the matrix in spiral order.

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

# Example 2:
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100

# Brute
# T.C. - O(m*n)
# S.C  - O(m*n)

# Intuition
# As you travel in a spiral fashion
# mark the cells in a visited set
# only go ahead if its not in visited
# or else change direction

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res: list[int] = []
        m, n = len(matrix), len(matrix[0])
        visited = set()
        total_steps = m * n

        row, col = 0, 0

        while total_steps > 0:
            # Left to Right
            while col < n and (row, col) not in visited:
                visited.add((row, col))
                res.append(matrix[row][col])
                col += 1
                total_steps -= 1
            row += 1
            col -= 1

            # Top to Bottom
            while row < m and (row, col) not in visited:
                visited.add((row, col))
                res.append(matrix[row][col])
                row += 1
                total_steps -= 1
            row -= 1
            col -= 1

            # Bottom Right to Bottom Left
            while col >= 0 and (row, col) not in visited:
                visited.add((row, col))
                res.append(matrix[row][col])
                col -= 1
                total_steps -= 1
            row -= 1
            col += 1

            # Bottom to Top
            while row >= 0 and (row, col) not in visited:
                visited.add((row, col))
                res.append(matrix[row][col])
                row -= 1
                total_steps -= 1
            row += 1
            col += 1

        return res


# Optimal
# T.C. - O(m*n)
# S.C  - O(1)

# Intuition
# Take 4 pointers left,right,top,bottom
# left,right will help us travel horizontally
# top,bottom will help us travel vertically
# Also suppose we have a matrix with one
# row only, we only require to print the
# left to right elements only

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, n - 1
        top, bottom = 0, m - 1
        res: list[int] = []

        while top <= bottom and left <= right:
            # Left to Right
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            # Top to Bottom
            for j in range(top, bottom + 1):
                res.append(matrix[j][right])
            right -= 1

            # Right to Left
            if top <= bottom:
                for k in range(right, left - 1, -1):
                    res.append(matrix[bottom][k])
                bottom -= 1

            # Bottom to Top
            if left <= right:
                for l in range(bottom, top - 1, -1):
                    res.append(matrix[l][left])
                left += 1

        return res
