# https://leetcode.com/problems/binary-search-tree-iterator/ , Medium

# Brute
# T.C. - O(n)
# S.C  - O(n)


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self._inorder = []

        def inorder(root):
            if root is None:
                return

            inorder(root.left)
            self._inorder.append(root.val)
            inorder(root.right)

        inorder(root)
        self.idx = 0

    def next(self) -> int:
        ans = self._inorder[self.idx]
        self.idx += 1
        return ans

    def hasNext(self) -> bool:
        if self.idx >= len(self._inorder):
            return False
        return True


# Optimal
# T.C. - O(1)
# S.C  - O(1)

# Algorithm
# Keep inserting all left elements in the stack
# When next function is called return top element of stack and check
# whether the node has a right child and start adding alll the left
# child as possible


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stk = []
        self.pushall(root)

    def next(self) -> int:
        tmpnode = self.stk.pop(-1)
        self.pushall(tmpnode.right)
        return tmpnode.val

    def hasNext(self) -> bool:
        if len(self.stk) == 0:
            return False
        return True

    def pushall(self, node):
        while node:
            self.stk.append(node)
            node = node.left
