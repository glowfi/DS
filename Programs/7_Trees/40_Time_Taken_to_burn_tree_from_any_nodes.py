# https://practice.geeksforgeeks.org/problems/burning-tree/1 , Hard


# Optimal
# T.C. - O(n)+O(n)
# S.C  - O(n)+O(n)

from collections import deque


class Solution:
    def minTime(self, root, target):
        parent = {}
        ref = {}

        def dfs(root, par):
            if root is None:
                return

            parent[root] = par
            ref[root.data] = root
            dfs(root.left, root)
            dfs(root.right, root)

        dfs(root, None)

        time = [-1]

        def bfs():
            q = deque([ref[target]])
            seen = {target: True}

            while q:
                for i in range(len(q)):
                    node = q.popleft()
                    seen[node] = True

                    if node.left and node.left not in seen:
                        q.append(node.left)
                    if node.right and node.right not in seen:
                        q.append(node.right)
                    if parent[node] and parent[node] not in seen:
                        q.append(parent[node])

                time[0] += 1

        bfs()
        return time[0]
