# https://practice.geeksforgeeks.org/problems/left-view-of-binary-tree/1 , Medium


# Optimal
# T.C. - O(n)
# S.C  - O(1)

from collections import deque


def LeftView(root):
    if not root:
        return []

    q = deque([root])
    ans = []

    while q:
        gotelement = False
        for i in range(len(q)):
            currNode = q.popleft()

            if not gotelement:
                gotelement = True
                ans.append(currNode.data)

            if currNode.left:
                q.append(currNode.left)
            if currNode.right:
                q.append(currNode.right)

    return ans
