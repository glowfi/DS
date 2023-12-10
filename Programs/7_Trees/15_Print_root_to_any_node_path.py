# NA , Medium


# Optimal
# T.C. - O(n)
# S.C  - O(n)


class Node:
    def __init__(self, val=-1, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def printroot2anyNodePath(self, root, tmp, ans, key):
        if root is None:
            return False

        tmp.append(root.val)
        if root.val == key:
            ans.append(tmp[:])
            return True

        left = self.printroot2anyNodePath(root.left, tmp, ans, key)
        if left:
            return True
        right = self.printroot2anyNodePath(root.right, tmp, ans, key)
        if right:
            return True
        tmp.pop(-1)
        return False


root = Node(1)
root.left = Node(2)
root.left.right = Node(5)
root.left.left = Node(4)

root.right = Node(3)
root.right.left = Node(9)
root.right.right = Node(6)
root.right.right.right = Node(8)
root.right.right.right.left = Node(88)


obj = Solution()
ans = []
obj.printroot2anyNodePath(root, [], ans, 8)
print(ans)
