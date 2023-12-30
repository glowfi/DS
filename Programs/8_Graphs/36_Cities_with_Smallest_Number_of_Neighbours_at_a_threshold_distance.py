# https://practice.geeksforgeeks.org/problems/city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/1 , Medium


# Using Floyd Warshall
# T.C. - O(V^3+V^2)
# S.C  - O(V^3)

from typing import List


class Solution:
    def findCity(
        self, n: int, m: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        matrix = []

        for i in range(n):
            tmp = []
            for j in range(n):
                if i == j:
                    tmp.append(0)
                else:
                    tmp.append(float("inf"))
            matrix.append(tmp)

        for u, v, wt in edges:
            matrix[u][v] = wt
            matrix[v][u] = wt

        for node in range(len(matrix)):
            for row in range(len(matrix)):
                for col in range(len(matrix[0])):
                    # mat[u][v] via node k -> mat[u][k]+mat[k][v]
                    currCost = matrix[row][node] + matrix[node][col]
                    matrix[row][col] = min(matrix[row][col], currCost)

        min_city = -1
        min_count = float("inf")

        for i in range(n):
            c = 0
            for j in range(n):
                if matrix[i][j] <= distanceThreshold:
                    c += 1
            if c <= min_count:
                min_count = c
                min_city = i

        return min_city


# Using Dijkstra
# Optimal
# T.C. - O(V*Elog(V)+V^2)
# S.C  - O(V^3)


from typing import List
import heapq


class Solution:
    def djk(self, adj, S):
        pq = [[0, S]]
        heapq.heapify(pq)
        dist = [float("inf") for _ in range(len(adj))]
        dist[S] = 0

        while pq:
            for _ in range(len(pq)):
                d, node = heapq.heappop(pq)

                for neighbour, wt in adj[node]:
                    if d + wt < dist[neighbour]:
                        heapq.heappush(pq, [d + wt, neighbour])
                        dist[neighbour] = d + wt

        return dist

    def findCity(
        self, n: int, m: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        adj = {i: [] for i in range(n)}
        ans = []

        for u, v, wt in edges:
            adj[u].append([v, wt])
            adj[v].append([u, wt])

        for i in range(n):
            ans.append(self.djk(adj, i))

        min_city = -1
        min_count = float("inf")

        for i in range(n):
            c = 0
            for j in range(n):
                if ans[i][j] <= distanceThreshold:
                    c += 1
            if c <= min_count:
                min_count = c
                min_city = i

        return min_city


# N = 4
# M = 4
# edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
# distanceThreshold = 4
# obj = Solution()
# print(obj.findCity(N, M, edges, distanceThreshold))
