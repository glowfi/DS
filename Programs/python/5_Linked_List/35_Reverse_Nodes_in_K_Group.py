# https://leetcode.com/problems/reverse-nodes-in-k-group , Hard, Recursion/Observation

# Question
# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.


# Example 1:
# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]

# Example 2:
# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]


# Constraints:

# The number of nodes in the list is n.
# 1 <= k <= n <= 5000
# 0 <= Node.val <= 1000


# Follow-up: Can you solve the problem in O(1) extra memory space?

# Brute
# T.C. - O(N)
# S.C  - O(K)

# Intuition
# first reach till k nodes
# keep a copy of current groups original head node
# then break link , take the last node in current group and make it point to None
# reverse the current linked list with original head node copy
# then make the original head node copy's next point to next K group reversed head
# Dont reverse if nodes are not equal to k or multiple of k


from typing import Optional


# Definition for singly-linked list.
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

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        start_node = head
        c = 1
        ptr = start_node
        while True:
            if not ptr.next or c == k:
                break
            c += 1
            ptr = ptr.next

        # Break Link
        nxtNode = None
        if ptr:
            nxtNode = ptr.next
            ptr.next = None

        # Reverse List
        if c % k == 0:
            rev_head = self.reverseList(start_node)

            # Recursively reverse next group
            start_node.next = self.reverseKGroup(nxtNode, k)

            return rev_head

        return start_node


# Optimal
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# Dont use recursion

from typing import Optional


# Definition for singly-linked list.
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

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        pass
