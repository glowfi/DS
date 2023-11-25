# https://leetcode.com/problems/unique-paths-ii/ , Medium

# Brute
# T.C. - O(n)
# S.C  - O(m*n) + O(n)


class Solution:
    def solve(self, x, y, m, n, grid):
        # Check inbounds
        if x >= m or y >= n:
            return 0

        if x < 0 or y < 0:
            return 0

        # Check obstacles
        if grid[x][y] == 1:
            return 0

        # Check destination
        if x == m - 1 and y == n - 1:
            return 1

        # Go down
        down = self.solve(x + 1, y, m, n, grid)

        # Go right
        right = self.solve(x, y + 1, m, n, grid)

        return down + right

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        return self.solve(0, 0, m, n, obstacleGrid)


# Better
# T.C. - O(n)
# S.C  - O(m*n) + O(n)


class Solution:
    def solve(self, x, y, m, n, grid, cache):
        # Check inbounds
        if x >= m or y >= n:
            return 0

        if x < 0 or y < 0:
            return 0

        # Check obstacles
        if grid[x][y] == 1:
            return 0

        # Check path already traversed
        if (x, y) in cache:
            return cache[(x, y)]

        # Check destination
        if x == m - 1 and y == n - 1:
            return 1

        # Go down
        down = self.solve(x + 1, y, m, n, grid, cache)

        # Go right
        right = self.solve(x, y + 1, m, n, grid, cache)

        cache[(x, y)] = down + right

        return cache[(x, y)]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        cache = {}
        return self.solve(0, 0, m, n, obstacleGrid, cache)
