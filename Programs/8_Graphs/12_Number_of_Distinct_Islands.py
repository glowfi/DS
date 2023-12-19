# https://www.geeksforgeeks.org/problems/number-of-distinct-islands/1 , Medium


# Optimal
# T.C. - O(n*m)
# S.C  - O(n*m)

import sys
from typing import List

sys.setrecursionlimit(10**8)


class Solution:
    def check_in_bounds(self, matrix, ro, co):
        if ro < 0 or co < 0:
            return False
        if ro >= len(matrix) or co >= len(matrix[0]):
            return False
        return True

    def dfs(self, ro, co, matrix, seen, tmp, base, st):
        if (
            not self.check_in_bounds(matrix, ro, co)
            or (ro, co) in seen
            or matrix[ro][co] == 0
        ):
            return

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        seen[(ro, co)] = True
        tmp.append((ro - base[0], co - base[1]))
        for dx, dy in dirs:
            self.dfs(ro + dx, co + dy, matrix, seen, tmp, base, st)

    def countDistinctIslands(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        seen = {}
        st = set()

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1 and (i, j) not in seen:
                    base = (i, j)
                    tmp = []
                    self.dfs(i, j, grid, seen, tmp, base, st)
                    st.add(tuple(tmp))

        return len(st)
