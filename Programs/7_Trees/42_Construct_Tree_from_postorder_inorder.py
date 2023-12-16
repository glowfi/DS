# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/ , Medium

# Optimal
# T.C. - O(n)
# S.C  - O(n)


class Solution:
    def helper(self, ino, post, inst, inen, psst, psen, seen):
        if inst > inen or psst > psen:
            return None

        currRoot = post[psen]
        root = TreeNode(currRoot)
        rootIndex = inst

        for i in range(inst, inen + 1):
            if ino[i] == currRoot and not seen[i]:
                rootIndex = i
                seen[i] = True
                break

        lfsize = rootIndex - inst
        rtsize = inen - rootIndex

        root.left = self.helper(
            ino, post, inst, rootIndex - 1, psst, psst + lfsize - 1, seen
        )
        root.right = self.helper(
            ino, post, rootIndex + 1, inen, psen - rtsize, psen - 1, seen
        )

        return root

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        seen = {idx: False for idx in range(len(inorder))}
        return self.helper(
            inorder, postorder, 0, len(inorder) - 1, 0, len(postorder) - 1, seen
        )


# from collections import deque

# def levelOrderBottom(root):
#     if not root:
#         return []

#     q = deque([root])
#     ans = []

#     while q:
#         curr_level = []
#         for _ in range(len(q)):
#             currNode = q.popleft()
#             curr_level.append(currNode.val)

#             if currNode.left:
#                 q.append(currNode.left)

#             if currNode.right:
#                 q.append(currNode.right)

#         ans.append(curr_level)

#     return ans


# obj = Solution()
# root = obj.buildTree([2, 1, 1, 2], [2, 1, 2, 1])
# print(levelOrderBottom(root))
