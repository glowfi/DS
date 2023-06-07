# https://leetcode.com/problems/set-matrix-zeroes/,Medium

# Brute
# T.C. -> O(n*m)*(O(n+m))+O(n*m)
# S.C. -> O(n)


class Solution:
    def markRow(self, row, matrix):
        for col in range(len(matrix[0])):
            if matrix[row][col] != 0:
                matrix[row][col] = float("-inf")

    def markCol(self, col, matrix):
        for row in range(len(matrix)):
            if matrix[row][col] != 0:
                matrix[row][col] = float("-inf")

    def setZeroes(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    # Mark current row
                    self.markRow(i, matrix)

                    # Mark current col
                    self.markCol(j, matrix)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == float("-inf"):
                    matrix[i][j] = 0

        return matrix


# Better
# T.C. -> O(n*m)+O(n*m)
# S.C. -> O(n)+O(m)


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = [0] * len(matrix)
        col = [0] * len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row[i] = 1
                    col[j] = 1

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if row[i] == 1 or col[j] == 1:
                    matrix[i][j] = 0

        return matrix


# Optimal
# T.C. -> O(n*m)+O(n*m)
# S.C. -> O(1)
