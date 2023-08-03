# https://leetcode.com/problems/delete-node-in-a-linked-list/,Medium

# Optimal
# T.C. -> O(1)
# S.C. -> O(1)


class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
