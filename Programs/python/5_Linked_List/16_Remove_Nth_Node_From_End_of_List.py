# https://leetcode.com/problems/remove-nth-node-from-end-of-list, Medium, Task

# Question
# Given the head of a linked list, remove the nth node from the end of the list and return its head.


# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Example 2:
# Input: head = [1], n = 1
# Output: []

# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]


# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz


# Follow up: Could you do this in one pass?

# Brute
# T.C. - O(N)+O(N)
# S.C  - O(1)

# Intuition
# Nth node from back is nothing but C-N from
# front where C is total length of list


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c = 0
        ptr = head

        while ptr:
            ptr = ptr.next
            c += 1

        ptr = head
        node_idx_to_delete = c - n
        if (node_idx_to_delete) == 0:
            return head.next

        while node_idx_to_delete != 1:
            ptr = ptr.next
            node_idx_to_delete -= 1

        if ptr and ptr.next:
            ptr.next = ptr.next.next

        return head


# Optimal
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# Goal is to first move a fast pointer by given n steps
# if fast becomes null then we were aksed to delete the first node
# Then move a slow and fast pointer simultenously until fast reaches last node
# You will see at the end the slow pointer will automatically reach the node
# just before the to be deleted node because we
# maintained an offset of n


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head

        for _ in range(n):
            fast = fast.next

        # was aksed to delete the head
        if not fast:
            return head.next

        slow = head

        # just stop when fast reach the last node
        while fast and fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return head
