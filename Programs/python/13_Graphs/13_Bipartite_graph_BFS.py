# https://leetcode.com/problems/is-graph-bipartite/ , Medium


# Optimal
# T.C. - O(n)
# S.C  - O(n)

from collections import deque


class Solution:
    def bfs(self, graph, color, src_node):
        q = deque([src_node])
        color[src_node] = 0

        while q:
            for i in range(len(q)):
                node = q.popleft()
                node_color = color[node]

                for currNode in graph[node]:
                    # if neighbour is colored check whether
                    # its its colored the opposite or not
                    if color[currNode] != -1:
                        if node_color == color[currNode]:
                            return False

                    # Or else color the node with opposite color
                    else:
                        color[currNode] = int(not node_color)
                        q.append(currNode)

        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1 for i in range(len(graph))]

        for i in range(len(graph)):
            if color[i] == -1:
                if not self.bfs(graph, color, i):
                    return False
        return True
