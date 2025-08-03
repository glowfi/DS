# https://leetcode.com/problems/rotate-list , Medium

# Question
# Given the head of a linked list, rotate the list to the right by k places.

# Example 1:
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]

# Example 2:
# Input: head = [0,1,2], k = 4
# Output: [2,0,1]


# Constraints:

# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 109

# Brute
# T.C. - O(N)+O(N^2)
# S.C  - O(1)

# Intuition
# mod k with length of linked list
# Keep rotating the linked list by one until you have rotated k times


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateByOne(self, head) -> Optional[ListNode]:
        ptr = head
        while ptr:
            if ptr.next and ptr.next.next is None:
                break
            ptr = ptr.next

        nxt = ptr.next
        ptr.next = None
        new_head = nxt
        new_head.next = head

        return new_head

    def get_length(self, head) -> int:
        n = 0
        ptr = head

        while ptr:
            ptr = ptr.next
            n += 1

        return n

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or head.next is None:
            return head

        k %= self.get_length(head)

        while k:
            head = self.rotateByOne(head)
            k -= 1

        return head


# Optimal
# T.C. - O(N)+O(N)
# S.C  - O(1)

# Intuition
# First find the length of linked list
# now move at n-k pos and make the node at (n-k) pos next to None
# make the tail point to head
# also make the new head as the node just next to node at (n-k) pos


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getLen(self, head) -> tuple[ListNode, int]:
        if not head:
            return head, 0

        n = 1
        ptr = head

        while ptr.next:
            ptr = ptr.next
            n += 1

        return ptr, n

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        last_node, n = self.getLen(head)
        if n == 0:
            return head

        k %= n
        if k == 0:
            return head

        target_node_pos = n - k
        c = 1
        ptr = head

        while ptr and c != target_node_pos:
            ptr = ptr.next
            c += 1

        new_head = ptr.next
        ptr.next = None
        last_node.next = head

        return new_head
