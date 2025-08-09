# https://www.geeksforgeeks.org/problems/delete-node-in-doubly-linked-list/1 , Easy, Basic

# Question
# Given a Doubly Linked list and a position. The task is to delete a node from a given position (position starts from 1) in a doubly linked list and return the head of the doubly Linked list.

# Examples:

# Input: LinkedList = 1 <--> 3 <--> 4, x = 3
# Output: 1 <--> 3
# Explanation: After deleting the node at position 3 (position starts from 1),the linked list will be now as 1 <--> 3.

# Input: LinkedList = 1 <--> 5 <--> 2 <--> 9, x = 1
# Output: 5 <--> 2 <--> 9
# Explanation:

# Constraints:
# 2 <= size of the linked list <= 10^6
# 1 <= x <= size of the linked list
# 1 <= node->data <= 10^4

# Optimal
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# Stop at the node to delete and save its reference to a variable
# then delete the following links:
# + make the delete nodes prev nodes next point to deleted nodes next
# + make the delete nodes next nodes prev point to deleted nodes prev


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None
        self.prev = None


class Solution:
    def delete_node(self, head: Node, x: int) -> Node:
        if x == 1:
            if head.next:
                head.next.prev = None
            return head.next

        ptr = head
        for _ in range(x - 1):
            ptr = ptr.next

        if ptr and ptr.prev:
            ptr.prev.next = ptr.next

        if ptr and ptr.next:
            ptr.next.prev = ptr.prev

        return head
