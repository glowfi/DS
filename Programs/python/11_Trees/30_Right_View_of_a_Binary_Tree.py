# https://leetcode.com/problems/binary-tree-right-side-view/ , Medium


# Optimal
# T.C. - O(n)
# S.C  - O(1)

from collections import deque


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque([root])
        ans = []

        while q:
            lastNode = None
            for i in range(len(q)):
                currNode = q.popleft()

                if currNode.left:
                    q.append(currNode.left)

                if currNode.right:
                    q.append(currNode.right)

                lastNode = currNode.val

            ans.append(lastNode)

        return ans
