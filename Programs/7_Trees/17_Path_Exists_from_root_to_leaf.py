# NA , Medium


# Optimal
# T.C. - O(n)
# S.C  - O(n)


# Given a path array-> [1,2,5] and root check if path exists from root to leaf


class Node:
    def __init__(self, val=-1, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def helper(root, tmpPath, targetPath):
    if root is None:
        return False

    tmpPath.append(root.val)
    if root.left is None and root.right is None:
        if tmpPath == targetPath:
            return True

    if helper(root.left, tmpPath, targetPath):
        return True
    if helper(root.right, tmpPath, targetPath):
        return True
    tmpPath.pop(-1)

    return False


def hasPath(root, targetPath):
    return helper(root, [], targetPath)


#    1
#   /\
#  2  3
# /\   \
# 4 5   6
#       \
#       8


root = Node(1)
root.left = Node(2)
root.left.right = Node(5)
root.left.left = Node(4)

root.right = Node(3)
root.right.right = Node(6)
root.right.right.right = Node(8)

print(hasPath(root, [1, 3, 6, 8]))
