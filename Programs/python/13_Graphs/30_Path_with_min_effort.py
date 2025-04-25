# https://leetcode.com/problems/path-with-minimum-effort/ , Medium

# Brute
# T.C. - O(n*n)
# S.C  - O(n*n)+O(n*n)+O(n*n)


class Solution:
    def check_in_bounds(self, matrix, ro, co):
        if ro < 0 or co < 0:
            return False
        if ro >= len(matrix) or co >= len(matrix[0]):
            return False
        return True

    def getMaxEffort(self, ls):
        mxEffort = float("-inf")

        for i in range(len(ls) - 1):
            mxEffort = max(mxEffort, ls[i + 1] - ls[i])

        return mxEffort

    def solve(self, r, c, grid, vis, tmp, ans):
        if not self.check_in_bounds(grid, r, c) or vis[r][c]:
            return

        if r == len(grid) - 1 and c == len(grid[0]) - 1:
            m, n = len(grid), len(grid[0])
            newTmp = [*tmp, grid[m - 1][n - 1]]
            effort = self.getMaxEffort(newTmp)
            ans[effort] = newTmp
            return

        vis[r][c] = True
        tmp.append(grid[r][c])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for dx, dy in dirs:
            curr_x = dx + r
            curr_y = dy + c
            self.solve(curr_x, curr_y, grid, vis, tmp, ans)

        vis[r][c] = False
        tmp.pop(-1)

    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        ans = {}
        vis = [[False for _ in range(n)] for _ in range(m)]
        self.solve(0, 0, heights, vis, [], ans)
        if min(ans.keys()) == float("-inf"):
            return 0
        return min(ans.keys())


# Optimal
# T.C. -
# S.C  -


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        pass
