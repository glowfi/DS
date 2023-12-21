# https://practice.geeksforgeeks.org/problems/topological-sort/1 , Medium

# Defination
# Linear ordering of vertices such that if there is
# an edge b/w u and v u appears before v in that
# Linear ordering

# Algorithm
# + Works only for DAG. Will get orderings of unsual length if DAG not used
# + Traverse the graph component wise
# + Take a visted array and only visit a node if not visted
# + Do a DFS traversal and put them into the STACK as you go back
# + Everything that is done will be stacked below

# Optimal
# T.C. - O(n)+O(n)
# S.C  - O(n)+O(n)


class Solution:
    def dfs(self, vis, adj, stk, src_node):
        vis[src_node] = 1
        for node in adj[src_node]:
            if not vis[node]:
                self.dfs(vis, adj, stk, node)

        stk.append(src_node)

    def topoSort(self, V, adj):
        ans = []
        vis = [0 for _ in range(V)]
        stk = []

        for i in range(V):
            if not vis[i]:
                self.dfs(vis, adj, stk, i)

        for i in range(len(stk)):
            data = stk.pop(-1)
            ans.append(data)

        return ans
