# https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1 , Medium

# Optimal
# T.C. - O(n^2)
# S.C  - O(n)


class Solution:
    def dfs(self, seen, path, adj, src_node):
        seen[src_node] = 1
        path[src_node] = 1
        for currNode in adj[src_node]:
            if path[currNode]:
                return True
            elif not seen[currNode]:
                if self.dfs(seen, path, adj, currNode):
                    return True

        path[src_node] = 0
        return False

    def isCyclic(self, V, adj):
        path = [0 for _ in range(V)]
        seen = [0 for _ in range(V)]

        for i in range(V):
            if not seen[i]:
                if self.dfs(seen, path, adj, i):
                    return True
        return False
