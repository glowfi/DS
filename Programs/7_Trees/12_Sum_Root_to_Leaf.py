# https://leetcode.com/problems/sum-root-to-leaf-numbers/ , Medium


# Optimal
# T.C. - O(n)
# S.C  - O(n)


class Solution:
    def helper(self, root, currNum):
        if root.left is None and root.right is None:
            currNum = (currNum * 10) + root.val
            self.sum += currNum
            return

        currNum = (currNum * 10) + root.val

        if root.left:
            self.helper(root.left, currNum)

        if root.right:
            self.helper(root.right, currNum)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        self.sum = 0
        self.helper(root, 0)
        return self.sum
