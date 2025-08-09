# https://www.geeksforgeeks.org/problems/insert-a-node-in-doubly-linked-list/1 , Easy, Basic

# Question
# Given a doubly-linked list, a position p, and an integer x. The task is to add a new node with value x at the position just after pth node in the doubly linked list and return the head of the updated list.

# Examples:

# Input: LinkedList: 2<->4<->5, p = 2, x = 6
# Output: 2<->4<->5<->6
# Explanation: p = 2, and x = 6. So, 6 is inserted after p, i.e, at position 2 (0-based indexing).

# Input: LinkedList: 1<->2<->3<->4, p = 0, x = 44
# Output: 1<->44<->2<->3<->4
# Explanation: p = 0, and x = 44 . So, 44 is inserted after p, i.e, at position 0 (0-based indexing).

# Constraints:
# 0 <= p < size of doubly linked list <= 10^6
# 1 <= x <= 10^6


# Optimal
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# Just stop at the given pth node
# then insert the node after the pth node
# assign required links


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None
        self.prev = None


class Solution:
    # Function to insert a new node at given position in doubly linked list.
    def addNode(self, head: Node, p: int, x: int) -> Node:
        ptr = head

        while p:
            p -= 1
            ptr = ptr.next

        new_node = Node(x)
        new_node.prev = ptr
        new_node.next = ptr.next

        if ptr.next:
            ptr.next.prev = new_node

        if ptr:
            ptr.next = new_node

        return head
