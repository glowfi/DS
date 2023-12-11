# https://leetcode.com/problems/count-good-nodes-in-binary-tree/ , Medium

# Optimal
# T.C. - O(n)
# S.C  - O(n)


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maxVal):
            if root is None:
                return

            if max(maxVal, root.val) == root.val:
                self.count += 1
                maxVal = max(maxVal, root.val)

            dfs(root.left, maxVal)
            dfs(root.right, maxVal)

        self.count = 0
        dfs(root, float("-inf"))
        return self.count
