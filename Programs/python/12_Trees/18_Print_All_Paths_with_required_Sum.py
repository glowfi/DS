# NA , Medium

# Optimal
# T.C. - O(n)
# S.C  - O(n)


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def helper(root, tmpPath, targetSum, ans):
    if root is None:
        return

    tmpPath.append(root.val)
    if targetSum - root.val == 0:
        ans.append(tmpPath[:])

    helper(root.left, tmpPath, targetSum - root.val, ans)
    helper(root.right, tmpPath, targetSum - root.val, ans)
    tmpPath.pop(-1)


def getAllPaths(root, ans, targetSum):
    if root is None:
        return

    helper(root, [], targetSum, ans)
    getAllPaths(root.left, ans, targetSum)
    getAllPaths(root.right, ans, targetSum)


#    1
#   / \
#  3  2
#    / \
#   1  3
#     /
#    2
#    \
#     2

ans = []

root = Node(1)
root.left = Node(3)
root.right = Node(2)
root.right.right = Node(3)
root.right.right.left = Node(2)
root.right.right.left.right = Node(2)
root.right.left = Node(1)
getAllPaths(root, ans, 4)
print(ans)
