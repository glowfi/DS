# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/ , Medium

# Optimal
# T.C. - O(n)
# S.C  - O(1)


from collections import deque


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])
        ans = deque([])

        while q:
            curr_level = []
            for _ in range(len(q)):
                currNode = q.popleft()
                curr_level.append(currNode.val)

                if currNode.left:
                    q.append(currNode.left)

                if currNode.right:
                    q.append(currNode.right)

            ans.appendleft(curr_level)

        return ans
