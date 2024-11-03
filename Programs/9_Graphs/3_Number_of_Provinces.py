# https://leetcode.com/problems/number-of-provinces/ , Medium


# Optimal
# T.C. - O(n*n)
# S.C  - O(n)

# Note : isConnected is an adjacency matrix


class Solution:
    def dfs(self, seen, src_node, adj):
        for node in adj[src_node]:
            if not seen[node]:
                seen[node] = True
                self.dfs(seen, node, adj)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        vertex = len(isConnected)
        seen = {i: False for i in range(vertex)}
        adj = {}
        self.c = 0

        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    if i not in adj:
                        adj[i] = [j]
                    else:
                        adj[i].append(j)

        for i in seen:
            if not seen[i]:
                seen[i] = True
                self.dfs(seen, i, adj)
                self.c += 1

        return self.c
