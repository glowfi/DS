# https://leetcode.com/problems/rotting-oranges/ , Medium


# Optimal
# T.C. - O(n^2)+O(n^2)
# S.C  - O(n)


from collections import deque


class Solution:
    def check_in_bounds(self, matrix, ro, co):
        if ro < 0 or co < 0:
            return False
        if ro >= len(matrix) or co >= len(matrix[0]):
            return False
        return True

    def orangesRotting(self, grid: List[List[int]]) -> int:
        frsh_count = 0
        q = deque([])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        seen = {}
        min_time = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    frsh_count += 1
                if grid[i][j] == 2:
                    q.append([i, j])
                    seen[(i, j)] = True

        while q and frsh_count > 0:
            for i in range(len(q)):
                ro, co = q.popleft()
                for dx, dy in dirs:
                    row = ro + dx
                    col = co + dy
                    if (
                        self.check_in_bounds(grid, row, col)
                        and (row, col) not in seen
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        seen[(row, col)] = True
                        q.append([row, col])
                        frsh_count -= 1
            min_time += 1

        if frsh_count == 0:
            return min_time
        return -1
