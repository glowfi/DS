# https://practice.geeksforgeeks.org/problems/minimum-spanning-tree/1 , Medium

# Optimal
# T.C. - O(E*logE)
# S.C  - O(E) + O(V)

# for every node, we are greedily selecting its
# unvisited adjacent node with the minimum edge weight(as the priority queue here is a min-heap and the
# topmost element is the node with the minimum edge weight). Doing so for every node, we can get
# the sum of all the edge weights of the minimum spanning tree and the spanning tree itself(if we wish to) as well.

import heapq


class Solution:
    def spanningTree(self, V, adj):
        vis = [0 for i in range(V)]
        # Weights,node
        pq = [[0, 0]]
        heapq.heapify(pq)
        sm = 0

        while pq:
            for i in range(len(pq)):
                wt, node = heapq.heappop(pq)

                if vis[node] == 1:
                    continue

                vis[node] = 1
                sm += wt

                for neighbours, wt in adj[node]:
                    if not vis[neighbours]:
                        heapq.heappush(pq, [wt, neighbours])

        return sm


g = [[[1, 5], [2, 1]], [[0, 5], [2, 3]], [[1, 3], [0, 1]]]
obj = Solution()
print(obj.spanningTree(3, g))
