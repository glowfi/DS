# https://www.geeksforgeeks.org/problems/inorder-successor-in-bst/1 , Easy

# Optimal
# T.C. - O(log(n))
# S.C  - O(log(n))


class Solution:
    def inorderSuccessor(self, root, x):
        self.insucc = float("inf")
        self.ans = None

        def ceil(root):
            if root is None:
                return

            if root.data > x.data:
                if root.data < self.insucc:
                    self.insucc = min(self.insucc, root.data)
                    self.ans = root

            if x.data < root.data:
                ceil(root.left)
            else:
                ceil(root.right)

        ceil(root)

        if self.ans is not None:
            return self.ans
        return Node(-1)
