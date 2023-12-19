# https://practice.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1 , Easy


# Directed Graph
# a->c
# |  |
# b  e
# |
# d-f

# Optimal [Recursive]
# T.C. - O(n)
# S.C  - O(n)

adj_ls = {"a": ["b", "c"], "b": ["d"], "c": ["e"], "d": ["f"], "e": [], "f": []}


def dfs_graph(adj_ls, source_node, tmp, ans):
    tmp.append(source_node)

    if not adj_ls[source_node]:
        ans.append(tmp[:])
        return

    for node in adj_ls[source_node]:
        dfs_graph(adj_ls, node, tmp, ans)
        tmp.pop(-1)


ans = []
dfs_graph(adj_ls, "a", [], ans)
print(ans)


# Optimal [Iterative]
# T.C. - O(n)
# S.C  - O(n)


def dfs_graph_iterative(adj_ls, source_node):
    stk = [source_node]

    while stk:
        node = stk.pop(-1)
        print(node)

        for currNode in adj_ls[node]:
            stk.append(currNode)


dfs_graph_iterative(adj_ls, "a")

# Optimal [GFG] [Recursive]
# T.C. - O(n)
# S.C  - O(n)


class Solution:
    def dfs(self, src_node, adj, seen, ans):
        for currNode in adj[src_node]:
            if not seen[currNode]:
                ans.append(currNode)
                seen[currNode] = True
                self.dfs(currNode, adj, seen, ans)

    def dfsOfGraph(self, V, adj):
        seen = {i: False for i in range(V)}
        seen[0] = True
        ans = [0]
        self.dfs(0, adj, seen, ans)
        return ans


# Optimal [GFG] [Iterative]
# T.C. - O(n)
# S.C  - O(n)


# User function Template for python3


class Solution:
    def dfs(self, adj, source_node, ans, seen):
        stk = [source_node]

        while stk:
            node = stk.pop(-1)
            if not seen[node]:
                ans.append(node)
                seen[node] = True
            for currNode in adj[node][::-1]:
                if not seen[currNode]:
                    stk.append(currNode)

    def dfsOfGraph(self, V, adj):
        ans = []
        seen = {i: False for i in range(V)}
        # seen[0] = True
        self.dfs(adj, 0, ans, seen)
        return ans
