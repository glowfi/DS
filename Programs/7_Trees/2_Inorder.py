# https://practice.geeksforgeeks.org/problems/inorder-traversal/1 , Easy

# Optimal
# T.C. - O(n)
# S.C  - O(n)


class Solution:
    def InOrder(self, root):
        if root is None:
            return []

        ans = []

        # Left
        l = self.InOrder(root.left)
        for i in l:
            ans.append(i)

        # Root
        ans.append(root.data)

        # Right
        r = self.InOrder(root.right)
        for j in r:
            ans.append(j)

        return ans


# Optimal [Iterative]
# T.C. - O(n)
# S.C  - O(1)

# Algorithm

# + Take a stack
# + Go as deep as possible to the left of the tree and keep adding node to the stack
# + If null pop the top of the stack
# + The go to the right of the poppped node
# + Repeat till stack empt


class Solution:
    def InOrder(self, root):
        if root is None:
            return []

        ans = []
        stack = []
        node = root

        while True:
            while node:
                stack.append(node)
                node = node.left

            if len(stack) == 0:
                break
            node = stack.pop(-1)
            ans.append(node.data)
            node = node.right
        return ans
