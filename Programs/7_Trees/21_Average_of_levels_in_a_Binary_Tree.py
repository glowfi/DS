# https://leetcode.com/problems/average-of-levels-in-binary-tree/ , Easy


# Optimal
# T.C. - O(n)
# S.C  - O(1)

from collections import deque


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        q = deque([root])
        ans = []

        while q:
            sum = 0
            node_count = 0
            for _ in range(len(q)):
                currNode = q.popleft()
                sum += currNode.val
                node_count += 1

                if currNode.left:
                    q.append(currNode.left)

                if currNode.right:
                    q.append(currNode.right)

            avg = sum / node_count
            ans.append(avg)

        return ans
