# https://www.geeksforgeeks.org/problems/kth-largest-element-in-bst/1 , Medium


# Optimal
# T.C. - O(n)
# S.C  - O(n)


class Solution:
    def kthLargest(self, root, k):
        c = [k]

        def inorder(root):
            if root is None:
                return -1

            r = inorder(root.right)
            if r != -1:
                return r

            c[0] -= 1
            if c[0] == 0:
                return root.data

            l = inorder(root.left)
            if l != -1:
                return l

            return -1

        return inorder(root)
