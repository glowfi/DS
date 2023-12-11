# https://leetcode.com/problems/kth-smallest-element-in-a-bst/ , Medium

# Brute
# T.C. - O(n)+O(n)
# S.C  - O(n)+O(n)


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ls = []

        def inorder(root):
            if root is None:
                return

            inorder(root.left)
            ls.append(root.val)
            inorder(root.right)

        inorder(root)
        return ls[k - 1]


# Optimal
# T.C. - O(n)
# S.C  - O(n)


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        c = [k]

        def inorder(root):
            if root is None:
                return -1

            l = inorder(root.left)
            if l != -1:
                return l

            c[0] -= 1
            if c[0] == 0:
                return root.val

            r = inorder(root.right)
            if r != -1:
                return r

            return -1

        return inorder(root)
