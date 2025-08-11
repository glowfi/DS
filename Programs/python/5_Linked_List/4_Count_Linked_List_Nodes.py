# https://www.geeksforgeeks.org/problems/count-nodes-of-linked-list/1, Easy, Basic

# Question
# Given a singly linked list. The task is to find the length of the linked list, where length is defined as the number of nodes in the linked list.

# Examples :

# Input: LinkedList : 1->2->3->4->5

# Output: 5
# Explanation: Count of nodes in the linked list is 5, which is its length.
# Input: LinkedList : 2->4->6->7->5->1->0

# Output: 7
# Explanation: Count of nodes in the linked list is 7. Hence, the output is 7.

# Expected Time Complexity: O(n)
# Expected Auxilliary Space: O(1)

# Constraints:
# 1 <= number of nodes <= 10^5
# 1 <= node->data <= 10^3


# Optimal
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# Keep traversing the linked list
# and keep counting the nodes till
# you reach a null node


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None


class Solution:
    def getCount(self, head: Node) -> int:
        ptr = head
        c = 0

        while ptr:
            ptr = ptr.next
            c += 1

        return c
