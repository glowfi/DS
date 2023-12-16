# https://practice.geeksforgeeks.org/problems/lowest-common-ancestor-in-a-binary-tree/1 , Medium

# p and q does may or may not exist

# Process a node after we have finished traversing
# its child node

# Optimal
# T.C. - O(n)
# S.C  - O(n)


class Solution:
    def lca(self, root, n1, n2):
        def dfs(root, n1, n2):
            if root is None:
                return None

            l, r = dfs(root.left, n1, n2), dfs(root.right, n1, n2)

            if root.data == n1 or root.data == n2:
                if root.data == n1:
                    self.p_found = True
                if root.data == n2:
                    self.q_found = True
                return root

            if l and r:
                return root

            return l or r

        self.p_found = False
        self.q_found = False
        k = dfs(root, n1, n2)

        if self.p_found and self.q_found:
            return k
        return None
