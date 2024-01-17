# https://leetcode.com/problems/minimum-falling-path-sum/ , Medium

# Recursion
# T.C. - O(n*m)
# S.C  - O(n+m)


class Solution:
    def check_in_bounds(self, m, n, max_row_size, max_col_size):
        if m < 0 or m >= max_row_size:
            return False
        if n < 0 or n >= max_col_size:
            return False
        return True

    def solve(self, i, j, m, n, matrix):
        # Base Case
        if not self.check_in_bounds(i, j, m, n):
            return float("inf")

        if i == m - 1:
            return matrix[i][j]

        # Hypo
        one = self.solve(i + 1, j - 1, m, n, matrix) + matrix[i][j]
        two = self.solve(i + 1, j, m, n, matrix) + matrix[i][j]
        three = self.solve(i + 1, j + 1, m, n, matrix) + matrix[i][j]

        return min(one, two, three)

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        self.mn = float("inf")

        for i in range(n):
            val = self.solve(0, i, m, n, matrix)
            self.mn = min(self.mn, val)

        return self.mn


# Memoization
# T.C. - O(n*m)
# S.C  - O(n*m)+O(n+m)


class Solution:
    def check_in_bounds(self, m, n, max_row_size, max_col_size):
        if m < 0 or m >= max_row_size:
            return False
        if n < 0 or n >= max_col_size:
            return False
        return True

    def solve(self, i, j, m, n, matrix, dp):
        # Base Case
        if not self.check_in_bounds(i, j, m, n):
            return float("inf")

        if (i, j) in dp:
            return dp[(i, j)]

        if i == m - 1:
            return matrix[i][j]

        # Hypo
        one = self.solve(i + 1, j - 1, m, n, matrix, dp) + matrix[i][j]
        two = self.solve(i + 1, j, m, n, matrix, dp) + matrix[i][j]
        three = self.solve(i + 1, j + 1, m, n, matrix, dp) + matrix[i][j]

        dp[(i, j)] = min(one, two, three)

        return dp[(i, j)]

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = {}
        self.mn = float("inf")

        for i in range(n):
            val = self.solve(0, i, m, n, matrix, dp)
            self.mn = min(self.mn, val)

        return self.mn


# Tabulation
# T.C. - O(n*m)
# S.C  - O(n*m)


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]

        for i in range(n):
            dp[m - 1][i] = matrix[m - 1][i]

        for i in range(m - 2, -1, -1):
            for j in range(n):
                one, two, three = float("inf"), float("inf"), float("inf")

                if i + 1 < m and j - 1 >= 0:
                    one = dp[i + 1][j - 1] + matrix[i][j]

                if i + 1 < m:
                    two = dp[i + 1][j] + matrix[i][j]

                if i + 1 < m and j + 1 < n:
                    three = dp[i + 1][j + 1] + matrix[i][j]

                dp[i][j] = min(one, two, three)

        self.mn = float("inf")
        for i in range(n):
            self.mn = min(dp[0][i], self.mn)

        return self.mn


# Space Optimized
# T.C. - O(n*m)
# S.C  - O(m)


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [-1 for _ in range(n)]

        for i in range(n):
            dp[i] = matrix[m - 1][i]

        for i in range(m - 2, -1, -1):
            tmp = [-1 for _ in range(n)]
            for j in range(n):
                one, two, three = float("inf"), float("inf"), float("inf")

                if i + 1 < m and j - 1 >= 0:
                    one = dp[j - 1] + matrix[i][j]

                if i + 1 < m:
                    two = dp[j] + matrix[i][j]

                if i + 1 < m and j + 1 < n:
                    three = dp[j + 1] + matrix[i][j]

                tmp[j] = min(one, two, three)
            dp = tmp

        self.mn = float("inf")
        for i in range(n):
            self.mn = min(dp[i], self.mn)

        return self.mn
