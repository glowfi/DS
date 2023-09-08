# https://leetcode.com/problems/rotate-image/description/,Medium

# Brute
# T.C. -> O(n*m)+O(n*m)
# S.C. -> O(n*m)


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        ncols = len(matrix[0]) - 1

        ans = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans[j][ncols] = matrix[i][j]
            ncols -= 1

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = ans[i][j]

        return matrix


# Optimal
# T.C. -> O(n/2*n/2)+O(n*n)
# S.C. -> O(1)


class Solution:
    def rev(self, row, mat):
        st, en = 0, len(mat[row]) - 1
        while st < en:
            mat[row][st], mat[row][en] = mat[row][en], mat[row][st]
            st += 1
            en -= 1

    def rotate(self, matrix: List[List[int]]) -> None:
        # Transpose
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix[0])):
                # Swap i,j and j,i
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse every rows
        for i in range(len(matrix)):
            self.rev(i, matrix)
            # matrix[i].reverse()

        return matrix
