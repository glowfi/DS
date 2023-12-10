# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/ , Medium


# Optimal
# T.C. - O(n)
# S.C  - O(1)

from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        q = deque([root])
        ans = []
        level_count = 0

        while q:
            curr_level = []
            for _ in range(len(q)):
                if level_count % 2 == 0:
                    node = q.popleft()
                    curr_level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                else:
                    node = q.pop()
                    curr_level.append(node.val)
                    if node.right:
                        q.appendleft(node.right)
                    if node.left:
                        q.appendleft(node.left)

            ans.append(curr_level)
            level_count += 1

        return ans
