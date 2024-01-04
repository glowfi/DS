# https://leetcode.com/problems/unique-paths-ii/ , Medium


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

    def solve(self, i, j, max_row_size, max_col_size, grid):
        if (
            not self.check_in_bounds(i, j, max_row_size, max_col_size)
            or grid[i][j] == 1
        ):
            return 0

        if i == 0 and j == 0:
            return 1

        # Go up
        down = self.solve(i - 1, j, max_row_size, max_col_size, grid)

        # Go Left
        right = self.solve(i, j - 1, max_row_size, max_col_size, grid)

        return down + right

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        return self.solve(m - 1, n - 1, m, n, obstacleGrid)


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
        if (
            not self.check_in_bounds(i, j, max_row_size, max_col_size)
            or grid[i][j] == 1
        ):
            return 0

        if (i, j) in dp:
            return dp[(i, j)]

        if i == 0 and j == 0:
            return 1

        # Go up
        up = self.solve(i - 1, j, max_row_size, max_col_size, grid, dp)

        # Go Left
        left = self.solve(i, j - 1, max_row_size, max_col_size, grid, dp)

        dp[(i, j)] = up + left

        return dp[(i, j)]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = {}
        return self.solve(m - 1, n - 1, m, n, obstacleGrid, dp)


# Tabulation
# T.C. - O(N*M)
# S.C  - O(N*M)


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1

        for row in range(m):
            for col in range(n):
                if obstacleGrid[row][col] == 1:
                    dp[row][col] = 0
                elif row == 0 and col == 0:
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
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0 for _ in range(n)]
        dp[0] = 1

        for row in range(m):
            tmp = [0 for _ in range(n)]
            for col in range(n):
                if obstacleGrid[row][col] == 1:
                    tmp[col] = 0
                elif row == 0 and col == 0:
                    tmp[col] = 1
                else:
                    up, left = 0, 0
                    if row - 1 >= 0:
                        up += dp[col]

                    if col - 1 >= 0:
                        left += tmp[col - 1]

                    tmp[col] = up + left

            dp = tmp

        return dp[n - 1]
