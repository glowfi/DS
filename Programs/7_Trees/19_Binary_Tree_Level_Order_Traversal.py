# https://leetcode.com/problems/binary-tree-level-order-traversal/ , Medium


# Optimal
# T.C. - O(n)
# S.C  - O(1)

from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root

        q = deque([root])
        ans = []

        while q:
            curr_level = []
            for i in range(len(q)):
                currNode = q.popleft()
                curr_level.append(currNode.val)

                if currNode.left:
                    q.append(currNode.left)

                if currNode.right:
                    q.append(currNode.right)

            ans.append(curr_level)

        return ans
