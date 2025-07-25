# https://www.geeksforgeeks.org/problems/reverse-a-doubly-linked-list/1 , Easy

# Question
# Given a doubly linked list. Your task is to reverse the doubly linked list and return its head.

# Examples:

# Input: LinkedList: 3 <-> 4 <-> 5
# Output: 5 <-> 4 <-> 3

# Input: LinkedList: 75 <-> 122 <-> 59 <-> 196
# Output: 196 <-> 59 <-> 122 <-> 75

# Expected Time Complexity: O(n).
# Expected Auxiliary Space: O(1).

# Constraints:
# 1 <= number of nodes <= 10^6
# 0 <= node->data <= 10^4


# Optimal
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# if you are at ith node make curr nodes
# next to prev and curr nodes prev to next node


class DLLNode:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


class Solution:
    def reverseDLL(self, head: DLLNode) -> DLLNode:
        prev = None
        ptr = head

        while ptr:
            next_node = ptr.next
            ptr.next = prev
            prev = ptr
            ptr.prev = next_node
            ptr = next_node

        return prev
