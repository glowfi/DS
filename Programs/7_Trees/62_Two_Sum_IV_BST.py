# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/ , Easy

# Optimal
# T.C. - O(n)
# S.C  - O(n)


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        h = {}

        def helper(root):
            if root is None:
                return False

            diff = k - root.val
            if diff in h:
                return True
            else:
                h[root.val] = True

            l = helper(root.left)
            if l:
                return True
            r = helper(root.right)
            if r:
                return True

            return False

        return helper(root)
