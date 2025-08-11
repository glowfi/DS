# https://leetcode.com/problems/spiral-matrix, Medium, Matrix

# Question
# Given an m x n matrix, return all elements of the matrix in spiral order.

# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:

# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]


# Optimal
# T.C. - O(N*M)
# S.C  - O(N*M)

# Intuition
# keep 4 pointes top,left,right,bottom
# just do what they have said till left<=right and top<=bottom


from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        left = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1

        ans = []

        while left <= right and top <= bottom:
            # Left to Right
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1

            # Top to Bottom
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1

            # Right to Left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1

            # Bottom to Top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1

        return ans
