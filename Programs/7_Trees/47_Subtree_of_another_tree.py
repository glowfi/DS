# https://leetcode.com/problems/subtree-of-another-tree/ , Easy


# Optimal
# T.C. - O(n*n)
# S.C  - O(n*n)


class Solution:
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True

        if p is not None and q is None:
            return False

        if q is not None and p is None:
            return False

        if p.val != q.val:
            return False

        l = self.isSameTree(p.left, q.left)
        if not l:
            return False
        r = self.isSameTree(p.right, q.right)
        if not r:
            return False

        return True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        if self.isSameTree(root, subRoot):
            return True

        l = self.isSubtree(root.left, subRoot)
        if l:
            return True

        r = self.isSubtree(root.right, subRoot)
        if r:
            return True

        return False
