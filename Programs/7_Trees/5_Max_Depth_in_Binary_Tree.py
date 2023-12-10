# https://leetcode.com/problems/maximum-depth-of-binary-tree/ , Easy


# Optimal
# T.C. - O(n)
# S.C  - O(n)


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base
        if root is None:
            return 0

        # Hypo
        leftTreeHeight = self.maxDepth(root.left)
        rightTreeHeight = self.maxDepth(root.right)

        # Induction
        return 1 + max(leftTreeHeight, rightTreeHeight)
