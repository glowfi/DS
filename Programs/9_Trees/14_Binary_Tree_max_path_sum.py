# https://leetcode.com/problems/binary-tree-maximum-path-sum/ , Hard


# Brute
# T.C. - O(n*n)
# S.C  - O(n)


class Solution:
    def helper1(self, root, currPathSum):
        if root is None:
            return 0

        currPathSum += root.val
        self.maxpathsum = max(self.maxpathsum, currPathSum)
        self.helper1(root.left, currPathSum)
        self.helper1(root.right, currPathSum)

    def maxPathSum_from_any_node_to_any(self, root):
        self.maxpathsum = float("-inf")
        self.helper1(root, 0)
        return self.maxpathsum

    def helper2(self, root):
        if root is None:
            return 0

        ls, rs = max(0, self.maxPathSum_from_any_node_to_any(root.left)), max(
            0, self.maxPathSum_from_any_node_to_any(root.right)
        )

        self.maxSum = max(self.maxSum, ls + rs + root.val)

        self.helper2(root.left)
        self.helper2(root.right)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float("-inf")
        self.helper2(root)
        return self.maxSum


# Optimal
# T.C. - O(n)
# S.C  - O(n)


# For each node check whats the maxpath sum we get by travelling in the
# right and left subtree


class Solution:
    def helper(self, root):
        if root is None:
            return 0

        max_path_sum_left = max(0, self.helper(root.left))
        max_path_sum_right = max(0, self.helper(root.right))

        self.maxSum = max(
            self.maxSum, root.val + max_path_sum_left + max_path_sum_right
        )

        return root.val + max(max_path_sum_left, max_path_sum_right)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float("-inf")
        self.helper(root)
        return self.maxSum
