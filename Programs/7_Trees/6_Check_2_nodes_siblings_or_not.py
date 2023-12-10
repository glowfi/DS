# NA , Medium


# Optimal
# T.C. - O(n*n)
# S.C  - O(n)


class Node:
    def __init__(self, val=-1, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def depthHelper(self, root, node, dep):
        if root is None:
            return 0

        if root == node:
            self._depth = dep
            return True

        l = self.depthHelper(root.left, node, dep + 1)
        if l:
            return True
        r = self.depthHelper(root.right, node, dep + 1)
        if r:
            return True
        return False

    def depth(self, root, node):
        self._depth = 0
        self.depthHelper(root, node, 0)
        return self._depth

    def check2siblings(self, root, p, q):
        if root is None:
            return False

        # For being siblings 2 nodes must have same parent and must be on same level(height)
        if root.left and root.right:
            if (
                root.left == p
                and root.right == q
                and self.depth(root, p) == self.depth(root, q)
            ):
                return True
            if (
                root.left == q
                and root.right == p
                and self.depth(root, p) == self.depth(root, q)
            ):
                return True

        left = self.check2siblings(root.left, p, q)
        if left:
            return True

        right = self.check2siblings(root.right, p, q)
        if right:
            return True

        return False


root = Node(1)
p = root.left = Node(2)
root.left.right = Node(5)
root.left.left = Node(4)

root.right = Node(3)
q = root.right.right = Node(6)
root.right.right.right = Node(8)


obj = Solution()
# Values in form of nodes
res = obj.check2siblings(root, p, q)
print(res)
