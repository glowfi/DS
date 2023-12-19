# https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1 , Medium

# Optimal
# T.C. - O(n)
# S.C  - O(n)

from typing import List
from collections import deque


class Solution:
    def bfs(self, adj, seen, src_node):
        q = deque([[src_node, -1]])

        while q:
            for _ in range(len(q)):
                node, parent = q.popleft()

                for currNode in adj[node]:
                    if currNode == parent:
                        continue
                    elif not seen[currNode]:
                        seen[currNode] = True
                        q.append([currNode, node])
                    elif seen[currNode]:
                        return True
        return False

    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        seen = {i: False for i in range(V)}

        for node in seen:
            if not seen[node]:
                if self.bfs(adj, seen, node):
                    return True
        return False
