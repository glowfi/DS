# https://leetcode.com/problems/search-in-a-binary-search-tree/ , Easy


# Optimal [Way 1]
# T.C. - O(log(n))
# S.C  - O(log(n)


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search(root):
            if root is None:
                return None

            node = None

            # if we got the value
            if root.val == val:
                return root

            # go left
            if val < root.val:
                node = search(root.left)
                if node:
                    return node

            # go right
            if val > root.val:
                node = search(root.right)
                if node:
                    return node

            return node

        return search(root)


# Optimal [Way 2]
# T.C. - O(log(n))
# S.C  - O(log(n)


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search(root):
            if root is None:
                return [root, False]

            node, found = None, False

            # if we got the value
            if root.val == val:
                return [root, True]

            # go left
            if val < root.val:
                node, found = search(root.left)
                if found:
                    return [node, found]

            # go right
            if val > root.val:
                node, found = search(root.right)
                if found:
                    return [node, found]

            return [node, found]

        return search(root)[0]
