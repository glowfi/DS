# https://leetcode.com/problems/minimum-path-sum/ , Medium


# Recursion
# T.C. - O(N*M)
# S.C  - O(N)+O(M)


class Solution:
    def check_in_bounds(self, m, n, max_row_size, max_col_size):
        if m < 0 or m >= max_row_size:
            return False
        if n < 0 or n >= max_col_size:
            return False
        return True

    def solve(self, i, j, max_row_size, max_col_size, grid):
        if not self.check_in_bounds(i, j, max_row_size, max_col_size):
            return float("inf")

        if i == 0 and j == 0:
            return grid[i][j]

        min_path_sum = float("inf")

        # Go up
        val = self.solve(i - 1, j, max_row_size, max_col_size, grid)
        if val + grid[i][j] < min_path_sum:
            min_path_sum = val + grid[i][j]

        # Go left
        val = self.solve(i, j - 1, max_row_size, max_col_size, grid)
        if val + grid[i][j] < min_path_sum:
            min_path_sum = val + grid[i][j]

        return min_path_sum

    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        return self.solve(m - 1, n - 1, m, n, grid)


# Memoization
# T.C. - O(N*M)
# S.C  - O(N*M)+O(N+M)


class Solution:
    def check_in_bounds(self, m, n, max_row_size, max_col_size):
        if m < 0 or m >= max_row_size:
            return False
        if n < 0 or n >= max_col_size:
            return False
        return True

    def solve(self, i, j, max_row_size, max_col_size, grid, dp):
        if not self.check_in_bounds(i, j, max_row_size, max_col_size):
            return float("inf")

        if (i, j) in dp:
            return dp[(i, j)]

        if i == 0 and j == 0:
            return grid[i][j]

        min_path_sum = float("inf")

        # Go up
        val = self.solve(i - 1, j, max_row_size, max_col_size, grid, dp)
        if val + grid[i][j] < min_path_sum:
            min_path_sum = val + grid[i][j]

        # Go left
        val = self.solve(i, j - 1, max_row_size, max_col_size, grid, dp)
        if val + grid[i][j] < min_path_sum:
            min_path_sum = val + grid[i][j]

        dp[(i, j)] = min_path_sum

        return dp[(i, j)]

    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = {}
        return self.solve(m - 1, n - 1, m, n, grid, dp)


# Tabulation
# T.C. - O(N*M)
# S.C  - O(N*M)


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[0][0] = grid[0][0]
                else:
                    up, left = float("inf"), float("inf")

                    if i - 1 >= 0:
                        up = dp[i - 1][j] + grid[i][j]

                    if j - 1 >= 0:
                        left = dp[i][j - 1] + grid[i][j]

                    dp[i][j] = min(up, left)

        return dp[m - 1][n - 1]


# Space Optimized
# T.C. - O(N*M)
# S.C  - O(M)


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0 for _ in range(n)]
        dp[0] = grid[0][0]

        for i in range(m):
            tmp = [0 for _ in range(n)]
            for j in range(n):
                if i == 0 and j == 0:
                    tmp[0] = grid[0][0]
                else:
                    up, left = float("inf"), float("inf")

                    if i - 1 >= 0:
                        up = dp[j] + grid[i][j]

                    if j - 1 >= 0:
                        left = tmp[j - 1] + grid[i][j]

                    tmp[j] = min(up, left)
            dp = tmp

        return dp[n - 1]
