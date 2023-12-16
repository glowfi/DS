# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/ , Medium


# Optimal
# T.C. - O(n)
# S.C  - O(n)


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        curr = root
        while True:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                break

        return curr
