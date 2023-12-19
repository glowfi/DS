# https://leetcode.com/problems/is-graph-bipartite/ , Medium


# Optimal
# T.C. - O(n)
# S.C  - O(n)+O(n)


class Solution:
    def dfs(self, graph, color, src_node):
        node_color = color[src_node]
        for currNode in graph[src_node]:
            # Check if currNode colored
            if color[currNode] != -1:
                if color[currNode] == node_color:
                    return False

            # Else color the node
            else:
                color[currNode] = int(not node_color)
                if not self.dfs(graph, color, currNode):
                    return False

        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1 for i in range(len(graph))]

        for i in range(len(graph)):
            if color[i] == -1:
                if not self.dfs(graph, color, i):
                    return False
        return True
