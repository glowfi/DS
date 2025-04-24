# https://leetcode.com/problems/balanced-binary-tree/ , Easy


# Optimal
# T.C. - O(n)
# S.C  - O(n)


# For being balanced :
# + Left subtree sould be balanced
# + Right subtree sould be balanced
# + Diff in height of left tree and right tree should be less than equals to 1


class Solution:
    def getHeight(self, root):
        if root is None:
            return 0

        lh, rh = self.getHeight(root.left), self.getHeight(root.right)

        return 1 + max(lh, rh)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        leftIsBalanced = self.isBalanced(root.left)
        rightIsBalanced = self.isBalanced(root.right)

        if not leftIsBalanced or not rightIsBalanced:
            return False

        lh, rh = self.getHeight(root.left), self.getHeight(root.right)
        if abs(lh - rh) >= 2:
            return False

        return True


# Optimal
# T.C. - O(n)
# S.C  - O(n)


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root is None:
                return [True, 0]

            isLeftBalanced, lh = dfs(root.left)
            isRightBalanced, rh = dfs(root.right)

            balanced = isLeftBalanced and isRightBalanced and abs(lh - rh) <= 1

            return [balanced, 1 + max(lh, rh)]

        return dfs(root)[0]
