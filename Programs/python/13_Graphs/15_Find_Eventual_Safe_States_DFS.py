# https://leetcode.com/problems/find-eventual-safe-states/ , Medium

# Brute
# T.C. - O(n^2)
# S.C  - O(n)+O(n)+O(n)


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

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V = len(graph)
        safe = []

        for i in range(V):
            path = [0 for _ in range(V)]
            seen = [0 for _ in range(V)]
            if not self.dfs(seen, path, graph, i):
                safe.append(i)

        return safe


# Optimal
# T.C. - O(n^2)
# S.C  - O(n)+O(n)+O(n)


class Solution:
    def dfs(self, seen, path, safe, adj, src_node):
        seen[src_node] = 1
        path[src_node] = 1

        for node in adj[src_node]:
            if path[node] and seen[node]:
                safe[node] = 0
                return True

            elif not seen[node]:
                if self.dfs(seen, path, safe, adj, node):
                    return True

        path[src_node] = 0
        safe[src_node] = 1

        return False

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        vertex = len(graph)

        seen, path, safe = (
            [0 for i in range(vertex)],
            [0 for i in range(vertex)],
            [0 for i in range(vertex)],
        )
        ans = []

        for node in range(vertex):
            if not seen[node]:
                self.dfs(seen, path, safe, graph, node)

        for i in range(len(safe)):
            if safe[i] == 1:
                ans.append(i)

        return ans
