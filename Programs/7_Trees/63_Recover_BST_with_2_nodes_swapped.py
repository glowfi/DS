# https://leetcode.com/problems/recover-binary-search-tree/ , Medium

# Brute
# T.C. - O(n)+O(n)+O(nlog(n))
# S.C  - O(n)+O(n)+O(n)


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def inorder(root):
            if root is None:
                return []

            ans = []

            l = inorder(root.left)
            for i in l:
                ans.append(i)

            ans.append(root.val)

            r = inorder(root.right)
            for i in r:
                ans.append(i)

            return ans

        sorted_list = inorder(root)
        sorted_list.sort()

        idx = [0]
        first, second = [None], [None]

        def _inorder(root, first, second):
            if root is None:
                return []

            l = _inorder(root.left, first, second)

            currIdx = idx[0]
            if sorted_list[currIdx] != root.val:
                if not first[0]:
                    first[0] = root
                else:
                    second[0] = root

            idx[0] += 1

            r = _inorder(root.right, first, second)

        _inorder(root, first, second)
        first[0].val, second[0].val = second[0].val, first[0].val


# Optimal
# T.C. - O(n)
# S.C  - O(n)


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        first, second = [None], [None]
        prev = [None]
        prevprev = [None]

        def inorder(root):
            if root is None:
                return

            inorder(root.left)
            if prev[0] is not None:
                if not root.val > prev[0].val:
                    if not first[0]:
                        first[0] = prev[0]
                        prevprev[0] = root
                    else:
                        second[0] = root
            prev[0] = root
            inorder(root.right)

        inorder(root)
        if first[0] and second[0]:
            first[0].val, second[0].val = second[0].val, first[0].val
        else:
            first[0].val, prevprev[0].val = prevprev[0].val, first[0].val
