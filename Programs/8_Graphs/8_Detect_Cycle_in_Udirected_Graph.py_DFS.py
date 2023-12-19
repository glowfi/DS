# https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1 , Medium

# Optimal
# T.C. - O(n)
# S.C  - O(n)

from typing import List
from collections import deque


class Solution:
    def dfs(self, adj, seen, src_node, parent):
        seen[src_node] = True
        for currNode in adj[src_node]:
            if currNode != parent:
                if not seen[currNode]:
                    seen[currNode] = True
                    if self.dfs(adj, seen, currNode, src_node):
                        return True
                else:
                    return True

        return False

    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        seen = {i: False for i in range(V)}

        for node in seen:
            if not seen[node]:
                if self.dfs(adj, seen, node, -1):
                    return True
        return False
