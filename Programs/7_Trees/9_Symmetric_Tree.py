# https://leetcode.com/problems/symmetric-tree/ , Easy


# Optimal
# T.C. - O(n)
# S.C  - O(n)


class Solution:
    def checkSymmetric(self, p, q):
        if p is None and q is None:
            return True

        if p is None and q is not None:
            return False

        if q is None and p is not None:
            return False

        if p.val != q.val:
            return False

        left_symmetric = self.checkSymmetric(p.left, q.right)
        right_symmetric = self.checkSymmetric(p.right, q.left)

        if left_symmetric and right_symmetric:
            return True
        return False

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.checkSymmetric(root.left, root.right)
