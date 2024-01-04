# https://leetcode.com/problems/unique-paths/ , Medium

# Recursion
# T.C. - O(N*M)
# S.C  - O(N+M)


class Solution:
    def check_in_bounds(self, m, n, max_row_size, max_col_size):
        if m < 0 or m >= max_row_size:
            return False
        if n < 0 or n >= max_col_size:
            return False
        return True

    def solve(self, i, j, max_row_size, max_col_size):
        if not self.check_in_bounds(i, j, max_row_size, max_col_size):
            return 0

        if i == 0 and j == 0:
            return 1

        # Go up
        down = self.solve(i - 1, j, max_row_size, max_col_size)

        # Go Left
        right = self.solve(i, j - 1, max_row_size, max_col_size)

        return down + right

    def uniquePaths(self, m: int, n: int) -> int:
        return self.solve(m - 1, n - 1, m, n)


# Memoization
# T.C. - O(N*M)
# S.C  - O(N+M)+O(N*M)


class Solution:
    def check_in_bounds(self, m, n, max_row_size, max_col_size):
        if m < 0 or m >= max_row_size:
            return False
        if n < 0 or n >= max_col_size:
            return False
        return True

    def solve(self, i, j, max_row_size, max_col_size, dp):
        if not self.check_in_bounds(i, j, max_row_size, max_col_size):
            return 0
        if dp[i][j] != -1:
            return dp[i][j]

        if i == 0 and j == 0:
            return 1

        # Go Up
        down = self.solve(i - 1, j, max_row_size, max_col_size, dp)

        # Go Left
        right = self.solve(i, j - 1, max_row_size, max_col_size, dp)

        dp[i][j] = down + right

        return dp[i][j]

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return self.solve(m - 1, n - 1, m, n, dp)


# Tabulation
# T.C. - O(N*M)
# S.C  - O(N*M)


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1

        for row in range(m):
            for col in range(n):
                if row == 0 and col == 0:
                    dp[0][0] = 1
                else:
                    up, left = 0, 0
                    if row - 1 >= 0:
                        up += dp[row - 1][col]

                    if col - 1 >= 0:
                        left += dp[row][col - 1]

                    dp[row][col] = up + left

        return dp[m - 1][n - 1]


# Space Optimized
# T.C. - O(N*M)
# S.C  - O(M)


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0 for _ in range(n)]

        for row in range(m):
            tmp = [0 for _ in range(n)]
            for col in range(n):
                if row == 0 and col == 0:
                    tmp[0] = 1
                else:
                    up, left = 0, 0
                    if row - 1 >= 0:
                        up += dp[col]

                    if col - 1 >= 0:
                        left += tmp[col - 1]

                    tmp[col] = up + left
            dp = tmp

        return dp[n - 1]
