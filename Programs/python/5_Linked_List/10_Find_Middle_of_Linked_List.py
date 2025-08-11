# https://leetcode.com/problems/middle-of-the-linked-list, Easy, FloydsAlgo

# Question
# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.


# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.

# Example 2:
# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.


# Constraints:

# The number of nodes in the list is in the range [1, 100].
# 1 <= Node.val <= 100

# Brute
# T.C. - O(N)+O(N) ~ O(N)
# S.C  - O(1)

# Intuition
# Find the length of linked list
# We know for finding the midpoint is length//2
# again traverse the linked list till length//2 times
# then the node at which we stop the traversal is the
# midpoint


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        ptr = head

        while ptr:
            length += 1
            ptr = ptr.next

        stop_pos = length // 2
        ptr = head

        while stop_pos:
            stop_pos -= 1
            ptr = ptr.next

        return ptr


# Optimal
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# We are going to use the floyds hare and tortoise algorithm
# We take slow and fast pointer where slow moves one step
# and fast pointer moves 2 steps. One thing to observe for
# odd and even length linked list
# For Odd length fast pointer will reach the last node before overshooting
# a->b->c->d->e->
#       s
#             f
#
# For even length fast pointer will overshoot
# a->b->c->d->
#       s
#             f


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
