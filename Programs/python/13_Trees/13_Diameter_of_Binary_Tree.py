# https://leetcode.com/problems/diameter-of-binary-tree/ , Easy

# Optimal
# T.C. - O(n)
# S.C  - O(n)


class Solution:
    def helper(self, root):
        if root is None:
            return 0

        lh, rh = self.helper(root.left), self.helper(root.right)
        self.diameter = max(self.diameter, lh + rh)

        return 1 + max(lh, rh)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.helper(root)
        return self.diameter
