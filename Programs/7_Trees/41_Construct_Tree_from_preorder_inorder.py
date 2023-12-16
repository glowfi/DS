# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/ , Medium


# Optimal
# T.C. - O(n*n)
# S.C  - O(n)


class Solution:
    def getRootIndex(self, arr, val):
        for i in range(len(arr)):
            if arr[i] == val:
                return i
        return -1

    def helper(self, idx: list[int], pre: list[int], ino: list[int]):
        currRoot = pre[idx[0]]
        root = TreeNode(currRoot)

        i = self.getRootIndex(ino, currRoot)

        leftTreeElements = ino[:i]
        if leftTreeElements:
            idx[0] += 1
            root.left = self.helper(idx, pre, leftTreeElements)

        rightTreeElements = ino[i + 1 :]
        if rightTreeElements:
            idx[0] += 1
            root.right = self.helper(idx, pre, rightTreeElements)

        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.helper([0], preorder, inorder)
