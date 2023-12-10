# NA , Medium


# Optimal
# T.C. - O(n)
# S.C  - O(1)

from collections import deque


class Node:
    def __init__(self, val=-1, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def levelOrderSuccesor(root, key):
    if root is None:
        return None

    if root.val == key:
        if root.left:
            return root.left
        if root.right:
            return root.right
        return None

    q = deque([root])

    ans = None
    stop = 0
    while q:
        for i in range(len(q)):
            currNode = q.popleft()

            if currNode.left:
                q.append(currNode.left)

            if currNode.right:
                q.append(currNode.right)

            if currNode.val == key:
                stop = 1
                ans = q[0].val
                break
        if stop == 1:
            break

    return ans


#        20
#     /      \
#    10       26
#   /  \     /   \
# 4     18  24    27
#      /  \
#     14   19
#    /  \
#   13  15

root = Node(20)
root.left = Node(10)
root.left.left = Node(4)
root.left.right = Node(18)
root.right = Node(26)
root.right.left = Node(24)
root.right.right = Node(27)
root.left.right.left = Node(14)
root.left.right.left.left = Node(13)
root.left.right.left.right = Node(15)
root.left.right.right = Node(19)

key = root.right.left  # node 24

print(levelOrderSuccesor(root, key.val))
