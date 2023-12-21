# https://practice.geeksforgeeks.org/problems/shortest-path-in-undirected-graph/1 , Medium

# Brute
# T.C. - O(n^2)
# S.C  - O(n)+O(n)

from typing import List
from collections import defaultdict


class Solution:
    def dfs(self, adj, src_node, dst_node, sm):
        if src_node == dst_node:
            self.sp = min(self.sp, sm)
            return

        for node, wt in adj[src_node]:
            self.dfs(adj, node, dst_node, sm + wt)

    def shortestPath(self, n: int, m: int, edges: List[List[int]]) -> List[int]:
        ans = [-1 for _ in range(n)]
        src_node = 0
        ans[src_node] = 0
        adj = defaultdict(list)

        for i in range(m):
            edge_weight = edges[i]
            adj[edge_weight[0]].append([edge_weight[1], edge_weight[2]])

        for i in range(1, n):
            self.sp = float("inf")
            self.dfs(adj, src_node, i, 0)
            if self.sp == float("inf"):
                self.sp = -1
            ans[i] = self.sp

        return ans


# Algorithm
# + Do topo sort
# + Take one node out of the stack and find distance of it in dist array lets say its distance as dst
# + Find the neighbouring nodes and update the distance as min(dist[i],dst+wt) where wt is edge wt b/w node and its neighbour node

# Optimal
# T.C. - O(n)+O(n)+O(n)
# S.C  - O(n)+O(n)+O(n)

from typing import List
from collections import deque
from collections import defaultdict


class Solution:
    def dfs(self, vis, adj, stk, src_node):
        vis[src_node] = 1
        for node, wt in adj[src_node]:
            if not vis[node]:
                self.dfs(vis, adj, stk, node)

        stk.append(src_node)

    def shortestPath(self, n: int, m: int, edges: List[List[int]]) -> List[int]:
        dist = [float("inf") for _ in range(n)]
        src_node = 0
        dist[src_node] = 0
        adj = defaultdict(list)

        for i in range(m):
            edge_weight = edges[i]
            adj[edge_weight[0]].append([edge_weight[1], edge_weight[2]])

        V = n

        vis = [0 for _ in range(V)]
        stk = []

        for i in range(V):
            if not vis[i]:
                self.dfs(vis, adj, stk, i)

        for i in range(len(stk)):
            data = stk.pop(-1)
            dst = dist[data]

            for neighbour, wt in adj[data]:
                dist[neighbour] = min(dist[neighbour], dst + wt)

        for i in range(len(dist)):
            if dist[i] == float("inf"):
                dist[i] = -1

        return dist


# obj = Solution()
# print(
#     obj.shortestPath(
#         6,
#         7,
#         [[0, 1, 2], [0, 4, 1], [4, 5, 4], [4, 2, 2], [1, 2, 3], [2, 3, 6], [5, 3, 1]],
#     )
# )
# print(obj.shortestPath(4, 2, [[0, 1, 2], [0, 2, 1]]))
