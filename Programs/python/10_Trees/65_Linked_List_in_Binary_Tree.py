# https://leetcode.com/problems/linked-list-in-binary-tree/description/ , Medium

# Brute
# T.C. - O(n^2)
# S.C  - O(n^2)


class Solution:
    def helper(self, root, ls, tmp):
        if root is None:
            return False

        tmp.append(root.val)
        if tmp == ls:
            return True

        l = self.helper(root.left, ls, tmp)
        if l:
            return True
        r = self.helper(root.right, ls, tmp)
        if r:
            return True
        tmp.pop(-1)

        return False

    def dfs(self, root, ls):
        if root is None:
            return False

        if self.helper(root, ls, []):
            return True

        l = self.dfs(root.left, ls)
        r = self.dfs(root.right, ls)

        return l or r

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        ls = []
        ptr = head

        while ptr:
            ls.append(ptr.val)
            ptr = ptr.next

        return self.dfs(root, ls)


# Optimal
# T.C. - O(n^2)
# S.C  - O(n)


class Solution:
    def helper(self, root, head):
        if head is None:
            return True

        if root is None:
            return False

        if root.val != head.val:
            return False

        l = self.helper(root.left, head.next)
        if l:
            return True
        r = self.helper(root.right, head.next)
        if r:
            return True

        return False

    def dfs(self, root, head):
        if root is None:
            return False

        if root.val == head.val:
            if self.helper(root, head):
                return True

        l = self.dfs(root.left, head)
        if l:
            return True
        r = self.dfs(root.right, head)
        if r:
            return True

        return False

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        return self.dfs(root, head)
