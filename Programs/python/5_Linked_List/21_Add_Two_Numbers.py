# https://leetcode.com/problems/add-two-numbers , Medium

# Question
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]


# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.


# Optimal
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# Just follow pure maths


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        ptr1, ptr2 = l1, l2

        new_head = ListNode()
        curr = new_head
        carry = 0

        while ptr1 and ptr2:
            sm = ptr1.val + ptr2.val + carry
            carry = sm // 10
            res = sm % 10
            curr.next = ListNode(res)

            curr = curr.next
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        while ptr1:
            sm = ptr1.val + carry
            carry = sm // 10
            res = sm % 10
            curr.next = ListNode(res)

            curr = curr.next
            ptr1 = ptr1.next

        while ptr2:
            sm = ptr2.val + carry
            carry = sm // 10
            res = sm % 10
            curr.next = ListNode(res)

            curr = curr.next
            ptr2 = ptr2.next

        if carry > 0:
            curr.next = ListNode(carry)

        return new_head.next
