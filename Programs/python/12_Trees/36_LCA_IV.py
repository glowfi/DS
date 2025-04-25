# NA , Medium


# Optimal
# T.C. - O(n)
# S.C  - O(n)


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", nodes: "List[TreeNode]"
    ) -> "TreeNode":
        nodes = set(nodes)

        def dfs(root):
            if root is None:
                return None

            # If we get p or q then we can stop the further calls and return
            # Because since p and q are guranteed to exist in the tree
            # we will find either p or q in the right ,we do not need to
            # check downwards any more
            if root in nodes:
                return root

            # Hypo
            l = dfs(root.left)  # Can we get p or q from left
            r = dfs(root.right)  # Can we get p or q from right

            # Current root is the LCA
            if l and r:
                return root

            # Node is the LCA itself
            return l or r
