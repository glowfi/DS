# https://practice.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1 , Medium

# Optimal
# T.C. - Elog(V)
# S.C  - O(E)+O(V)

# Why no queue is used because we will kind of explore all paths and then find the minimal we end up exploring too many paths
# But in dijkstra we go kinda greedy every time we pick the node with minimal distance

import heapq


class Solution:
    def dijkstra(self, V, adj, S):
        dist = [float("inf") for _ in range(V)]
        dist[S] = 0

        pq = [[0, S]]
        heapq.heapify(pq)

        while pq:
            for _ in range(len(pq)):
                d, node = heapq.heappop(pq)

                for neighbour, wt in adj[node]:
                    if d + wt < dist[neighbour]:
                        heapq.heappush(pq, [d + wt, neighbour])
                        dist[neighbour] = d + wt
        return dist


# V = 3
# adj = [[[1, 1], [2, 6]], [[2, 3], [0, 1]], [[1, 3], [0, 6]]]
# S = 2
# obj = Solution()
# print(obj.dijkstra(V, adj, S))
