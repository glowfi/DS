# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/ , Medium


# Optimal
# T.C. - O(n)+O(n)
# S.C  - O(n)+O(n)

from collections import deque


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}
        ans = []

        def dfs(root, par):
            if root is None:
                return

            parent[root] = par
            dfs(root.left, root)
            dfs(root.right, root)

        dfs(root, None)

        seen = {}

        def bfs(k):
            q = deque([target])
            seen = {target: True}

            while q:
                for i in range(len(q)):
                    node = q.popleft()
                    seen[node] = True
                    if k == 0:
                        ans.append(node.val)

                    if node.left and node.left not in seen:
                        q.append(node.left)
                    if node.right and node.right not in seen:
                        q.append(node.right)
                    if parent[node] and parent[node] not in seen:
                        q.append(parent[node])
                k -= 1

        bfs(k)
        return ans
