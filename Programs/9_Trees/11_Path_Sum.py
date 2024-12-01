# https://leetcode.com/problems/path-sum, Easy

# Optimal
# T.C. - O(n)
# S.C  - O(n)


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Base case
        if root is None:
            return False

        if root.left is None and root.right is None:
            if targetSum - root.val == 0:
                return True

        # Induction & Hypothesis

        left = self.hasPathSum(root.left, targetSum - root.val)
        if left:
            return True
        right = self.hasPathSum(root.right, targetSum - root.val)
        if right:
            return True

        return False
