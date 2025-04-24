# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/ , Medium


# Optimal
# T.C. - O(n)
# S.C  - O(1)

from collections import deque


class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        if not root:
            return root
        q = deque([root])

        while q:
            curr_level = []
            for i in range(len(q)):
                currNode = q.popleft()
                curr_level.append(currNode)

                if currNode.left:
                    q.append(currNode.left)

                if currNode.right:
                    q.append(currNode.right)

            for node in range(len(curr_level) - 1):
                curr_level[node].next = curr_level[node + 1]

            curr_level[len(curr_level) - 1].next = None

        return root
