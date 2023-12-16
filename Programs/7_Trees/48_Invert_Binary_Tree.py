# https://leetcode.com/problems/invert-binary-tree/ , Easy


# Optimal
# T.C. - O(n)
# S.C  - O(n)


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base Case
        if root is None:
            return root

        # Hypo
        l, r = self.invertTree(root.left), self.invertTree(root.right)

        # Induction
        root.left, root.right = r, l

        return root
