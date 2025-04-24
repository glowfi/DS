# https://practice.geeksforgeeks.org/problems/strongly-connected-components-kosarajus-algo/1 , Medium


# Optimal
# T.C. - O(V+E)+O(V+E)+O(V+E)
# S.C  - O(3V)


# Algorithm

# + Sort them according to their finishing time as they complete append them in a stack
# + Reverse the edges in the graph
# + Do a dfs


class Solution:
    def dfs(self, src_node, adj, stk, seen):
        seen[src_node] = True
        for nei in adj[src_node]:
            if not seen[nei]:
                self.dfs(nei, adj, stk, seen)

        stk.append(src_node)

    def _dfs(self, src_node, adj, seen):
        if src_node not in adj:
            return
        seen[src_node] = True
        for nei in adj[src_node]:
            if not seen[nei]:
                self._dfs(nei, adj, seen)

    def kosaraju(self, V, adj):
        stk = []
        seen = {i: False for i in range(V)}

        # Sorting
        for i in range(V):
            if not seen[i]:
                self.dfs(i, adj, stk, seen)

        # Reverse the edges
        new_adj = {}
        for ind, node in enumerate(adj):
            for nei in adj[ind]:
                if nei not in new_adj:
                    new_adj[nei] = [ind]
                else:
                    new_adj[nei].append(ind)

        # Do a dfs
        new_seen = {i: False for i in range(V)}
        scc = 0

        while stk:
            node = stk.pop(-1)
            if not new_seen[node]:
                self._dfs(node, new_adj, new_seen)
                scc += 1

        return scc


obj = Solution()
adj = [[2, 3], [0], [1], [4], []]
V = 5
V = 2
adj = [[1], []]
print(obj.kosaraju(V, adj))
