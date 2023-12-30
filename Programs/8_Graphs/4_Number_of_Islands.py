# https://leetcode.com/problems/number-of-islands/ , Medium

# Better
# T.C. - O(n*n)
# S.C  - O(n)

# Note :grid is not an adjacency matrix its a binary grid


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(ro, co, grid, seen):
            if (
                ro < 0
                or co < 0
                or ro >= len(grid)
                or co >= len(grid[0])
                or (ro, co) in seen
                or grid[ro][co] == "0"
            ):
                return

            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            seen[(ro, co)] = True

            for dx, dy in dirs:
                x = dx + ro
                y = dy + co
                dfs(x, y, grid, seen)

        seen = {}
        c = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in seen and grid[i][j] == "1":
                    dfs(i, j, grid, seen)
                    c += 1

        return c


# Optimal
# T.C. - O(n^2)+O(n^2)
# S.C  - O(1)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(ro, co, grid):
            if ro < 0 or co < 0:
                return

            if ro >= len(grid) or co >= len(grid[0]):
                return

            if grid[ro][co] != "1":
                return

            grid[ro][co] = "#"

            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

            for dx, dy in dirs:
                dfs(ro + dx, co + dy, grid)

        self.c = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j, grid)
                    self.c += 1

        return self.c
