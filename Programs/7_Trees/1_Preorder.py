# https://practice.geeksforgeeks.org/problems/preorder-traversal/1 , Easy

# Optimal [Recursive]
# T.C. - O(n)
# S.C  - O(n)


def preorder(root):
    if root is None:
        return []

    ans = []

    # Root
    ans.append(root.data)

    # Left
    l = preorder(root.left)
    for i in l:
        ans.append(i)

    # Right
    r = preorder(root.right)
    for j in r:
        ans.append(j)

    return ans


# Optimal [Iterative]
# T.C. - O(n)
# S.C  - O(1)


# Algorithm

# + Take a stack and initialize it with the root node
# + Pop the element from the top of stack
# + Insert the right child first and the second child second
# + Continue the iteration unitl stack gets empty


def preorder(root):
    if root is None:
        return []

    ans = []
    stack = [root]

    while stack:
        node = stack.pop(-1)

        ans.append(node.data)

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)

    return ans
