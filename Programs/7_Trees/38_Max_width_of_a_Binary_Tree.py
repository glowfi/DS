# https://leetcode.com/problems/maximum-width-of-binary-tree/ , Medium

# Optimal
# T.C. - O(n)
# S.C  - O(1)

from collections import deque


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque([[root, 0]])
        maxWidth = float("-inf")

        while q:
            maxWidth = max(maxWidth, (q[-1][1] - q[0][1]) + 1)
            for i in range(len(q)):
                node, idx = q.popleft()

                if node.left:
                    q.append([node.left, 2 * idx + 1])

                if node.right:
                    q.append([node.right, 2 * idx + 2])

        return maxWidth
