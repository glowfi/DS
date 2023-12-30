# https://practice.geeksforgeeks.org/problems/number-of-islands/1 , Medium


# Brute
# T.C. - O(k*m*m)
# S.C  -

from typing import List


class Solution:
    def numIslands(self, grid: List[List[int]]) -> int:
        def dfs(seen, ro, co, grid):
            if ro < 0 or co < 0:
                return

            if ro >= len(grid) or co >= len(grid[0]):
                return

            if grid[ro][co] == 0:
                return

            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

            for dx, dy in dirs:
                if (ro + dx, co + dy) not in seen:
                    seen[(ro + dx, co + dy)] = True
                    dfs(seen, ro + dx, co + dy, grid)

        seen = {}
        self.c = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in seen:
                    seen[(i, j)] = True
                    dfs(seen, i, j, grid)
                    self.c += 1

        return self.c

    def numOfIslands(
        self, rows: int, cols: int, operators: List[List[int]]
    ) -> List[int]:
        ans = []
        mat = [[0 for _ in range(cols)] for _ in range(rows)]

        for i in range(len(operators)):
            x, y = operators[i][0], operators[i][1]
            mat[x][y] = 1
            k = self.numIslands(mat)
            ans.append(k)

        return ans


# Optimal
# T.C. -
# S.C  -

from typing import List


class Solution:
    def numOfIslands(
        self, rows: int, cols: int, operators: List[List[int]]
    ) -> List[int]:
        pass


obj = Solution()
n = 4
m = 5
k = 4
A = [[1, 1], [0, 1], [3, 3], [3, 4]]
# A = [[0, 0], [1, 1], [2, 2], [3, 3]]
print(obj.numOfIslands(n, m, A))
