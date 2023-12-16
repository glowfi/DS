# NA, Easy

# Optimal
# T.C. - O(log(n))
# S.C  - O(log(n))


class Solution:
    def inorderPredeccessor(self, root, x):
        self.inpred = float("-inf")
        self.ans = None

        def floor(root):
            if root is None:
                return

            if root.data < x.data:
                if root.data < self.inpred:
                    self.inpred = max(self.inpred, root.data)
                    self.ans = root

            if x.data < root.data:
                floor(root.left)
            else:
                floor(root.right)

        floor(root)

        if self.ans is not None:
            return self.ans
        return Node(-1)
