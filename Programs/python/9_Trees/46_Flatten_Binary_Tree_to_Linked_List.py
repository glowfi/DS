# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/ , Medium

# Brute
# T.C. - O(n)+O(n)
# S.C  - O(n)+O(n)


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def preorder(root):
            if root is None:
                return []

            ans = []
            ans.append(root.val)

            l = preorder(root.left)
            for i in l:
                ans.append(i)

            r = preorder(root.right)
            for i in r:
                ans.append(i)

            return ans

        ret = preorder(root)
        newroot = TreeNode(-1)
        cp = newroot

        for i in ret:
            newroot.right = TreeNode(i)
            newroot = newroot.right

        root = cp.right


# Optimal
# T.C. -
# S.C  -
