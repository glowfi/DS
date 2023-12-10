# NA  , Medium


# Optimal
# T.C. - O(n)
# S.C  - O(n)


# Algorithm


class Node:
    def __init__(self, val=-1, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def allTraversal(root):
    pre, ino, post = [], [], []
    stack = [[root, 1]]

    while stack:
        node, num = stack.pop(-1)

        if num == 1:
            # Go to pre-order final list
            pre.append(node.val)

            # Insert with ++
            stack.append([node, num + 1])

            # go to left
            if node.left:
                stack.append([node.left, 1])

        elif num == 2:
            # Go to in-order final list
            ino.append(node.val)

            # Insert with ++
            stack.append([node, num + 1])

            # go to right
            if node.right:
                stack.append([node.right, 1])
        else:
            # Go to in-order final list
            post.append(node.val)

    print(pre)
    print(ino)
    print(post)


#    3
#  /   \
# 5     1
# / \  / \
# 6  2 0 8


root = Node(3)
root.left = Node(5)
root.right = Node(1)
root.right.right = Node(8)
root.right.left = Node(0)
root.left.right = Node(2)
root.left.left = Node(6)

allTraversal(root)
