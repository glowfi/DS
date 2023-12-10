# https://www.geeksforgeeks.org/problems/postorder-traversal/1 , Easy

# Optimal [Recursive]
# T.C. - O(n)
# S.C  - O(n)


def postOrder(root):
    if root is None:
        return []

    ans = []

    # Left
    l = postOrder(root.left)
    for i in l:
        ans.append(i)

    # Right
    r = postOrder(root.right)
    for i in r:
        ans.append(i)

    # Root
    ans.append(root.data)

    return ans


# Optimal [Iterative]
# T.C. - O(n)
# S.C  - O(n)

# Algorithm
# + Take a stack and initialize with root node
# + We are going to reach as left as possible and keep adding nodes in the stack
# + On reaching null we backtrack like recursion but here we pop the top node and go to its right
# + If thr popped nodes right becomes null then again pop the top of the stack
# + Run a while loop with ondition stack not empty and top of the stack.right is equal to tmp
# + Keep popping the top of the stack
# + Append in the post order


def postOrder(root):
    curr = root
    stack = []
    ans = []

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left

        tmp = stack[-1].right
        if tmp is None:
            tmp = stack[-1]
            stack.pop(-1)
            ans.append(tmp.data)
            while stack and tmp == stack[-1].right:
                tmp = stack[-1]
                stack.pop(-1)
                ans.append(tmp.data)

        else:
            curr = tmp

    return ans
