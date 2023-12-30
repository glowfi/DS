# https://leetcode.com/problems/shortest-path-in-binary-matrix/ , Medium

# Better
# T.C. - O(Elog(n*n))
# S.C  - O(n*n)+O(n*n)


import heapq


class Solution:
    def check_in_bounds(self, x, y, grid):
        if x >= len(grid) or x < 0 or y >= len(grid[0]) or y < 0:
            return False
        return True

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1:
            return -1

        pq = [(1, (0, 0))]
        heapq.heapify(pq)

        dist = [[float("inf") for _ in range(n)] for _ in range(n)]
        dist[0][0] = 1
        vis = [[False for _ in range(n)] for _ in range(n)]

        while pq:
            for i in range(len(pq)):
                curr_dist, node = heapq.heappop(pq)
                x, y = node
                vis[x][y] = True

                dirs = [
                    [1, 0],
                    [0, 1],
                    [-1, 0],
                    [0, -1],
                    [1, 1],
                    [-1, -1],
                    [1, -1],
                    [-1, 1],
                ]

                for dx, dy in dirs:
                    curr_x, curr_y = dx + x, dy + y
                    if (
                        self.check_in_bounds(curr_x, curr_y, grid)
                        and not vis[curr_x][curr_y]
                        and grid[curr_x][curr_y] == 0
                    ):
                        if curr_dist + 1 < dist[curr_x][curr_y]:
                            heapq.heappush(pq, (curr_dist + 1, (curr_x, curr_y)))
                            dist[curr_x][curr_y] = curr_dist + 1

        if dist[n - 1][n - 1] == float("inf"):
            return -1

        return dist[n - 1][n - 1]


# Optimal
# T.C. - O(Elog(n*n))
# S.C  - O(n*n)


from collections import deque


class Solution:
    def check_in_bounds(self, x, y, grid):
        if x >= len(grid) or x < 0 or y >= len(grid[0]) or y < 0:
            return False
        return True

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1:
            return -1

        pq = deque([(1, (0, 0))])

        dist = [[float("inf") for _ in range(n)] for _ in range(n)]
        dist[0][0] = 1

        while pq:
            for i in range(len(pq)):
                curr_dist, node = pq.popleft()
                x, y = node

                dirs = [
                    [1, 0],
                    [0, 1],
                    [-1, 0],
                    [0, -1],
                    [1, 1],
                    [-1, -1],
                    [1, -1],
                    [-1, 1],
                ]

                for dx, dy in dirs:
                    curr_x, curr_y = dx + x, dy + y
                    if (
                        self.check_in_bounds(curr_x, curr_y, grid)
                        and grid[curr_x][curr_y] == 0
                    ):
                        if curr_dist + 1 < dist[curr_x][curr_y]:
                            if curr_x == n - 1 and curr_y == n - 1:
                                return curr_dist + 1
                            pq.append((curr_dist + 1, (curr_x, curr_y)))
                            dist[curr_x][curr_y] = curr_dist + 1

        if dist[n - 1][n - 1] == float("inf"):
            return -1

        return dist[n - 1][n - 1]
