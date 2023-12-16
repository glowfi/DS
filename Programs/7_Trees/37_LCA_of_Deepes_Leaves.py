# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/ , Medium

# Brute
# T.C. - O(n)+O(n)+O(nlog(n))
# S.C  - O(n)+O(n)


class Solution:
    def getDeepestLeaves(self, root, ans, height, mxHeight):
        if root is None:
            return

        if root.left is None and root.right is None:
            if height >= mxHeight:
                mxHeight = height
                ans.append((height, root))

        self.getDeepestLeaves(root.left, ans, height + 1, mxHeight)
        self.getDeepestLeaves(root.right, ans, height + 1, mxHeight)

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Get the leaves nodes and sort them according to height
        nodes = []
        self.getDeepestLeaves(root, nodes, 0, float("-inf"))
        nodes.sort(reverse=True, key=lambda x: x[0])

        for h, val in nodes:
            maxH = h
            break
        tmpnodes = set(nodes)

        # Keep the leaf node only with max height
        nodez = set()
        for h, val in tmpnodes:
            if h == maxH:
                nodez.add(val)

        # If only one node return that node
        if len(nodez) == 1:
            return list(nodez)[0]

        # Find lca otherwise
        def dfs(node):
            if node is None:
                return None

            if node in nodez:
                return root

            l = dfs(node.left)
            r = dfs(node.right)

            if l and r:
                return node

            return l or r

        return dfs(root)
