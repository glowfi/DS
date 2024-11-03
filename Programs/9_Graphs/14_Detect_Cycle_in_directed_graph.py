# https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1 , Medium

# Optimal
# T.C. - O(n^2)
# S.C  - O(n)


class Solution:
    def dfs(self, seen, path, adj, src_node):
        seen[src_node] = 1
        path[src_node] = 1

        for node in adj[src_node]:
            if path[node] and seen[node]:
                return True

            elif not seen[node]:
                if self.dfs(seen, path, adj, node):
                    return True

        path[src_node] = 0
        return False

    def isCyclic(self, V, adj):
        path = [0 for i in range(V)]
        seen = [0 for i in range(V)]

        for node in range(V):
            if not seen[node]:
                if self.dfs(seen, path, adj, node):
                    return True

        return False
