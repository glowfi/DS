# https://practice.geeksforgeeks.org/problems/check-if-two-nodes-are-cousins/1 , Medium


# Optimal
# T.C. - O(n)+O(n)
# S.C  - O(n)


# For 2 nodes being cousins the should:
# + diff parent
# + at the same level


def helper(root, node, parent, depth):
    if root is None:
        return [parent, depth, 0]

    if root.data == node:
        return [parent, depth, 1]

    l = helper(root.left, node, root, depth + 1)
    if l[-1] == 1:
        return l
    r = helper(root.right, node, root, depth + 1)
    if r[-1] == 1:
        return r
    return [parent, depth, 0]


def isCousin(root, a, b):
    parent_of_a, depth_of_a, _ = helper(root, a, None, 1)
    parent_of_b, depth_of_b, _ = helper(root, b, None, 1)

    if parent_of_a != parent_of_b and depth_of_a == depth_of_b:
        return True
    return False
