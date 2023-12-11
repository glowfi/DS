# https://leetcode.com/problems/validate-binary-search-tree/ , Medium

# Brute
# T.C. - O(n*avg_node_insubtree)
# S.C  - O(n*avg_node_insubtree)


class Solution:
    def checkLeftSmaller(self, root, val):
        if root is None:
            return True

        if root.val >= val:
            return False

        return self.checkLeftSmaller(root.left, val) and self.checkLeftSmaller(
            root.right, val
        )

    def checkRightGreater(self, root, val):
        if root is None:
            return True

        if root.val <= val:
            return False

        return self.checkRightGreater(root.left, val) and self.checkRightGreater(
            root.right, val
        )

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        c1 = self.checkLeftSmaller(root.left, root.val)
        if not c1:
            return False
        c2 = self.checkRightGreater(root.right, root.val)
        if not c2:
            return False

        return self.isValidBST(root.left) and self.isValidBST(root.right)


# Optimal
# T.C. - O(n)
# S.C  - O(n)


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, lower, higher):
            if root is None:
                return True

            if not lower < root.val or not root.val < higher:
                return False

            return dfs(root.left, lower, root.val) and dfs(root.right, root.val, higher)

        return dfs(root, float("-inf"), float("inf"))
