# https://www.geeksforgeeks.org/problems/largest-bst/1 , Medium

# Brute
# T.C. - O(n*n)+O(n)
# S.C  - O(n*n)+O(n)


class Solution:
    def is_dataid_bst(self, root):
        def dfs(root, lower, higher):
            if root is None:
                return True

            if not lower < root.data or not root.data < higher:
                return False

            return dfs(root.left, lower, root.data) and dfs(
                root.right, root.data, higher
            )

        return dfs(root, float("-inf"), float("inf"))

    def count_nodes(self, root):
        if root is None:
            return 0

        l = self.count_nodes(root.left)
        r = self.count_nodes(root.right)

        return 1 + l + r

    def largestBst(self, root):
        def helper(root):
            if root is None:
                return 0

            if self.is_dataid_bst(root):
                getSize = self.count_nodes(root)
                self.largetSize = max(self.largetSize, getSize)

            helper(root.left)
            helper(root.right)

        self.largetSize = float("-inf")
        helper(root)
        return self.largetSize


# Optimal
# T.C. - O(n)
# S.C  - O(n)


class Nodeval:
    def __init__(self, min, max, max_node_count):
        self.min = min
        self.max = max
        self.max_node_count = max_node_count


class Solution:
    def largestBst(self, root):
        def helper(root):
            if root is None:
                return Nodeval(float("inf"), float("-inf"), 0)

            if root.left is None and root.right is None:
                return Nodeval(root.data, root.data, 1)

            left = helper(root.left)
            right = helper(root.right)

            if root.data > left.max and root.data < right.min:
                return Nodeval(
                    min(
                        root.data,
                        left.min,
                    ),
                    max(root.data, right.max),
                    1 + left.max_node_count + right.max_node_count,
                )
            return Nodeval(
                float("-inf"),
                float("inf"),
                max(left.max_node_count, right.max_node_count),
            )

        return helper(root).max_node_count
