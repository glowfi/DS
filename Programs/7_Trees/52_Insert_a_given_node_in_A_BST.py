# https://leetcode.com/problems/insert-into-a-binary-search-tree/ , Medium


# Optimal
# T.C. - O(log(n))
# S.C  - O(log(n))


class Solution:
    def _insert(self, root, val):
        if root is None:
            return root

        if val < root.val:
            if root.left is None:
                root.left = TreeNode(val)
            else:
                self._insert(root.left, val)

        else:
            if root.right is None:
                root.right = TreeNode(val)
            else:
                self._insert(root.right, val)

        return root

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            root = TreeNode(val)
            return root
        else:
            return self._insert(root, val)
