# https://www.geeksforgeeks.org/problems/root-to-leaf-paths/1 , Medium


# Optimal
# T.C. - O(n)
# S.C  - O(n)


class Node:
    def _init_(self, val):
        self.data = val
        self.left = None
        self.right = None


def helper(root, tmp, ans):
    if root is None:
        return

    tmp.append(root.data)
    if root.left is None and root.right is None:
        ans.append(tmp[:])

    helper(root.left, tmp, ans)
    helper(root.right, tmp, ans)
    tmp.pop(-1)


def Paths(root):
    ans = []
    helper(root, [], ans)
    return ans
