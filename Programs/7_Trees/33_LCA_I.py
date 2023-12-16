# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/ , Medium


# Optimal
# T.C. - O(n)
# S.C  - O(n)


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if root is None:
            return None

        # If we get p or q then we can stop the further calls and return
        # Because since p and q are guranteed to exist in the tree
        # we will find either p or q in the right ,we do not need to
        # check downwards any more
        if root == p or root == q:
            return root

        # Hypo
        l = self.lowestCommonAncestor(root.left, p, q)  # Can we get p or q from left
        r = self.lowestCommonAncestor(root.right, p, q)  # Can we get p or q from right

        # Current root is the LCA
        if l and r:
            return root

        # Node is the LCA itself
        return l or r
