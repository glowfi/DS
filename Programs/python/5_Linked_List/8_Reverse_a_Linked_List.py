# https://leetcode.com/problems/reverse-linked-list, Easy, Basic

# Question
# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:
# Input: head = [1,2]
# Output: [2,1]

# Example 3:
# Input: head = []
# Output: []


# Constraints:

# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000

# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?


# Optimal
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# if you are at ith node make the curr nodes
# next point to prev node

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev


# Optimal
# T.C. - O(N)
# S.C  - O(N)

# Intuition
# if you are at ith node make the curr nodes
# next point to prev node

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rev_linked_list(curr: ListNode, prev: ListNode) -> Optional[ListNode]:
            if curr is None:
                return prev

            next_node = curr.next
            curr.next = prev
            prev = curr
            return rev_linked_list(next_node, prev)

        return rev_linked_list(head, None)
