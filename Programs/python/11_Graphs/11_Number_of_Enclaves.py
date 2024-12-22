# https://leetcode.com/problems/number-of-enclaves/ , Medium

# Optimal
# T.C. - O(N) + O(M) + O(NxMx4)
# S.C  - O(N x M), O(N x M)


class Solution:
    def check_in_bounds(self, grid, ro, co):
        if ro < 0 or co < 0:
            return False
        if ro >= len(grid) or co >= len(grid[0]):
            return False
        return True

    def dfs(self, ro, co, grid, seen):
        if (
            not self.check_in_bounds(grid, ro, co)
            or grid[ro][co] == 0
            or (ro, co) in seen
        ):
            return

        seen[(ro, co)] = True
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for dx, dy in dirs:
            self.dfs(dx + ro, dy + co, grid, seen)

    def numEnclaves(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        seen = {}
        self.c = 0

        # First row
        for i in range(c):
            if grid[0][i] == 1 and (0, i) not in seen:
                self.dfs(0, i, grid, seen)

        # Last row
        for i in range(c):
            if grid[r - 1][i] == 1 and (r - 1, i) not in seen:
                self.dfs(r - 1, i, grid, seen)

        # First Column
        for i in range(r):
            if grid[i][0] == 1 and (i, 0) not in seen:
                self.dfs(i, 0, grid, seen)

        # Last Column
        for i in range(r):
            if grid[i][c - 1] == 1 and (i, c - 1) not in seen:
                self.dfs(i, c - 1, grid, seen)

        for i in range(r):
            for j in range(c):
                if (i, j) not in seen and grid[i][j] == 1:
                    self.c += 1
        return self.c
