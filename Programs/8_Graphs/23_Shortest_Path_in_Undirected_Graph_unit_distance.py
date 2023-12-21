# https://practice.geeksforgeeks.org/problems/shortest-path-in-undirected-graph-having-unit-distance/1 , Medium

# Brute
# T.C. - O(n^2)
# S.C  - O(n)+O(n)

from typing import List
from collections import defaultdict


class Solution:
    def dfs(self, adj, src_node, dst_node, sm, parent, vis, tmp, path):
        tmp.append(src_node)
        if src_node == dst_node:
            # print(tmp, "dst")
            self.sp = min(self.sp, sm)
            return

        vis[src_node] = 1
        path[src_node] = 1

        for node, wt in adj[src_node]:
            if (node == parent) or (path[node] and vis[node]) == 1:
                continue
            elif not vis[node]:
                self.dfs(adj, node, dst_node, sm + wt, src_node, vis, tmp, path)
                tmp.pop(-1)

        path[src_node] = 0
        vis[src_node] = 0

    def shortestPath(self, edges, n, m, src):
        ans = [-1 for _ in range(n)]
        ans[src] = 0
        adj = defaultdict(list)

        for i in range(m):
            edge_weight = edges[i]
            adj[edge_weight[0]].append([edge_weight[1], 1])
            if [edge_weight[0], 1] not in adj[edge_weight[1]]:
                adj[edge_weight[1]].append([edge_weight[0], 1])

        # print(adj)

        for i in range(n):
            if i == src:
                continue
            else:
                self.sp = float("inf")
                vis = [0 for _ in range(n)]
                path = [0 for _ in range(n)]
                # print(src, i)
                self.dfs(adj, src, i, 0, -1, vis, [], path)
                if self.sp == float("inf"):
                    self.sp = -1
                ans[i] = self.sp

        return ans


# Optimal
# T.C. - O(n)
# S.C  - O(n)

from collections import deque
from collections import defaultdict


class Solution:
    def shortestPath(self, edges, n, m, src):
        dist = [float("inf") for _ in range(n)]
        dist[src] = 0
        adj = defaultdict(list)

        for i in range(m):
            edge_weight = edges[i]
            adj[edge_weight[0]].append([edge_weight[1], 1])
            if [edge_weight[0], 1] not in adj[edge_weight[1]]:
                adj[edge_weight[1]].append([edge_weight[0], 1])

        q = deque([[src, 0, -1]])
        seen = [0 for _ in range(n)]
        seen[src] = 1

        while q:
            for i in range(len(q)):
                node, _dist, parent = q.popleft()

                for neighbour, wt in adj[node]:
                    if (neighbour == parent) or (
                        seen[neighbour] and neighbour != parent
                    ):
                        continue
                    else:
                        seen[node] = 1
                        dist[neighbour] = min(_dist + wt, dist[neighbour])
                        q.append([neighbour, _dist + wt, node])

        for i in range(len(dist)):
            if dist[i] == float("inf"):
                dist[i] = -1

        return dist


obj = Solution()
print(
    obj.shortestPath(
        [
            [0, 1],
            [0, 3],
            [3, 4],
            [4, 5],
            [5, 6],
            [1, 2],
            [2, 6],
            [6, 7],
            [7, 8],
            [6, 8],
        ],
        9,
        10,
        0,
    )
)

print(
    obj.shortestPath(
        [
            [1, 5],
            [1, 6],
            [2, 0],
            [3, 3],
            [4, 0],
            [4, 6],
            [5, 3],
            [5, 4],
            [6, 5],
            [6, 6],
        ],
        7,
        10,
        4,
    )
)
