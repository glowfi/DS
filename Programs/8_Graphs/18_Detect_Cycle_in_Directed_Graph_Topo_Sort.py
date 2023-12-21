# https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1  , Medium

# Optimal
# T.C. - O(n)+O(n)
# S.C  - O(n)+O(n)


from collections import deque


class Solution:
    def isCyclic(self, V, adj):
        indeg = [0 for _ in range(V)]

        for i in range(V):
            for j in adj[i]:
                indeg[j] += 1

        q = deque([])
        ans = []

        for i in range(V):
            if indeg[i] == 0:
                q.append(i)

        while q:
            for _ in range(len(q)):
                node = q.popleft()

                # Node in topoSort so remove indeegrees of neighbouring nodes
                ans.append(node)

                for neighbour in adj[node]:
                    indeg[neighbour] -= 1

                    if indeg[neighbour] == 0:
                        q.append(neighbour)

        for i in range(len(indeg)):
            if indeg[i] != 0:
                return True

        return False
