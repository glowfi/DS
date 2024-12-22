# https://www.geeksforgeeks.org/problems/bfs-traversal-of-graph/1 , Easy


# Directed Graph
# a->c
# |  |
# b  e
# |
# d-f

# Optimal [Iterative]
# T.C. - O(n)
# S.C  - O(n)

from collections import deque

adj_ls = {"a": ["b", "c"], "b": ["d"], "c": ["e"], "d": ["f"], "e": [], "f": []}


def bfs(adj_ls, source_node):
    q = deque([source_node])

    while q:
        for i in range(len(q)):
            node = q.popleft()
            print(node)
            for currNode in adj_ls[node]:
                q.append(currNode)


bfs(adj_ls, "a")


# Optimal [GFG]
# T.C. - O(n)
# S.C  - O(n)

from typing import List
from queue import Queue
from collections import deque


class Solution:
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        q = deque([0])
        seen = {i: False for i in range(V)}
        seen[0] = True
        ans = []

        while q:
            for i in range(len(q)):
                node = q.popleft()
                ans.append(node)

                for currNode in adj[node]:
                    if not seen[currNode]:
                        seen[currNode] = True
                        q.append(currNode)

        return ans
