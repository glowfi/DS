# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/ , Hard


# Memoization
# T.C. - O(4^n)
# S.C  - O(n)+O(n^3)


class Solution:
    def solve(self, i, j, matrix, preVal, dp):
        if (i, j, preVal) in dp:
            return dp[(i, j, preVal)]

        if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]):
            return 0

        if matrix[i][j] <= preVal:
            return 0

        t, d, l, r = 0, 0, 0, 0

        # Top
        t = 1 + self.solve(i - 1, j, matrix, matrix[i][j], dp)

        # Down
        d = 1 + self.solve(i + 1, j, matrix, matrix[i][j], dp)

        # Left
        l = 1 + self.solve(i, j - 1, matrix, matrix[i][j], dp)

        # Right
        r = 1 + self.solve(i, j + 1, matrix, matrix[i][j], dp)

        dp[(i, j, preVal)] = max(t, d, l, r)

        return dp[(i, j, preVal)]

    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        mx = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                getVal = self.solve(row, col, matrix, -1, {})
                mx = max(mx, getVal)
        return mx
