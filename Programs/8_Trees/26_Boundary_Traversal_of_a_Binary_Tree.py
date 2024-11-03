# https://www.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/1 , Medium

# Optimal
# T.C. - O(n)+O(n)+O(n)
# S.C  - O(1)


class Solution:
    def leftBoundary_without_leaf_node(self, root, ans):
        while True:
            if root.left is None and root.right is None:
                break
            ans.append(root.data)
            if root.left:
                root = root.left
            else:
                root = root.right

    def rightBoundary_without_leaf_node(self, root, ans):
        while True:
            if root.left is None and root.right is None:
                break
            ans.append(root.data)
            if root.right:
                root = root.right
            else:
                root = root.left

    def leafnodes(self, root, ans):
        if root is None:
            return

        if root.left is None and root.right is None:
            ans.append(root.data)

        self.leafnodes(root.left, ans)
        self.leafnodes(root.right, ans)

    def printBoundaryView(self, root):
        if not root:
            return []
        if root.left is None and root.right is None:
            return [root.data]

        ans = [root.data]

        ans2 = []
        if root.left:
            self.leftBoundary_without_leaf_node(root.left, ans)
        self.leafnodes(root, ans)
        if root.right:
            self.rightBoundary_without_leaf_node(root.right, ans2)
            ans2 = ans2[::-1]

        for i in ans2:
            ans.append(i)
        return ans
