# https://leetcode.com/problems/odd-even-linked-list, Medium, Task

# Question
# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
# The first node is considered odd, and the second node is even, and so on.
# Note that the relative order inside both the even and odd groups should remain as it was in the input.
# You must solve the problem in O(1) extra space complexity and O(n) time complexity.


# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]

# Example 2:
# Input: head = [2,1,3,5,6,4,7]
# Output: [2,3,6,7,1,5,4]


# Constraints:
# The number of nodes in the linked list is in the range [0, 10^4].
# -10^6 <= Node.val <= 10^6

# Brute
# T.C. - O(N)+O(N)
# S.C  - O(1)

# Intuition
# keep a new_head
# traverse the given head and put the odd index to the new_head first
# traverse again in the given head and put the even index to the new_head second


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode()
        curr_new_head = new_head
        ptr = head
        idx = 1

        while ptr:
            if idx % 2 == 1:
                curr_new_head.next = ListNode(ptr.val)
                curr_new_head = curr_new_head.next
            ptr = ptr.next
            idx += 1

        ptr = head
        idx = 1

        while ptr:
            if idx % 2 == 0:
                curr_new_head.next = ListNode(ptr.val)
                curr_new_head = curr_new_head.next
            ptr = ptr.next
            idx += 1

        return new_head.next


# Optimal
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# take 2 nodes odd,even and even head
# 1  2  3  4  5
# a->b->c->d->e->
# o  e
# o  eh
# goal is to make the current odd index node point to next odd index node
# and make the current event index node point to next even index node


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        odd, even = head, head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = even.next.next
            even = even.next

        odd.next = even_head

        return head
