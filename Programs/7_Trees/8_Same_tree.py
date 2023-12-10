# https://leetcode.com/problems/same-tree/ , Easy


# Optimal
# T.C. - O(n)
# S.C  - O(n)


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base Case
        if p is None and q is None:
            return True

        if p is None and q is not None:
            return False

        if q is None and p is not None:
            return False

        if p.val != q.val:
            return False

        # Hypo
        left_same = self.isSameTree(p.left, q.left)
        right_same = self.isSameTree(p.right, q.right)

        # Induction
        if left_same and right_same:
            return True
        return False
