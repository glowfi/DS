# https://leetcode.com/problems/rotate-image, Medium, Matrix

# Question
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the
# input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.


# Example 1:

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
# Example 2:


# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

# Optimal
# T.C. - O(2*N*M) ~ O(N*M)
# S.C  - O(1)

# Intuition
# Do transpose of a matrix
# Reverse every row


from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Transpose the matrix
        for i in range(len(matrix)):
            for j in range(
                i + 1, len(matrix[0])
            ):  # swap values above diagonal to avoid overwriting
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse each row
        for i in range(len(matrix)):
            j = 0
            while j < len(matrix[0]) // 2:
                n = len(matrix[0])
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]
                j += 1
