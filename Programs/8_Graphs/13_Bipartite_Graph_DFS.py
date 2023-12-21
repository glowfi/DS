# https://leetcode.com/problems/is-graph-bipartite/ , Medium


# Optimal
# T.C. - O(n)
# S.C  - O(n)+O(n)


class Solution:
    def dfs(self, col, adj, src_node):
        for node in adj[src_node]:
            # If colored check colored with parent/source node
            if col[node] != -1 and col[src_node] == col[node]:
                return False

            # Else color the node
            elif col[node] == -1:
                col[node] = int(not col[src_node])
                if not self.dfs(col, adj, node):
                    return False
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        col = [-1 for i in range(len(graph))]

        for node in range(len(graph)):
            if col[node] == -1:
                col[node] = 0
                if not self.dfs(col, graph, node):
                    return False

        return True
