# https://www.geeksforgeeks.org/problems/linked-list-insertion-1587115620/1 , Easy

# Question
# Given the head of a Singly Linked List and a value x, insert that value x at the end of the LinkedList and return the modified Linked List.

# Examples :

# Input: LinkedList: 1->2->3->4->5 , x = 6
# Output: 1->2->3->4->5->6
# Explanation:

# We can see that 6 is inserted at the end of the linkedlist.
# Input: LinkedList: 5->4 , x = 1
# Output: 5->4->1
# Explanation:

# We can see that 1 is inserted at the end of the linkedlist.

# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(1)

# Constraints:
# 0 <= number of nodes <= 10^5
# 1 <= node->data , x <= 10^3


# Optimal
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# Just keep traversing the link list
# and stop just at the last nodes reference
# now we have last nodes reference and must
# make the last node next point to the new
# created node


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None


class Solution:
    def insertAtEnd(self, head: Node, x: int) -> Node:
        if head is None:
            return Node(x)

        ptr = head

        while ptr.next:
            ptr = ptr.next

        ptr.next = Node(x)

        return head
