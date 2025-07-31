# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list , Medium

# Question
# You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

# The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

# For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.


# Example 1:
# Input: head = [1,3,4,7,1,2,6]
# Output: [1,3,4,1,2,6]
# Explanation:
# The above figure represents the given linked list. The indices of the nodes are written below.
# Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
# We return the new list after removing this node.

# Example 2:
# Input: head = [1,2,3,4]
# Output: [1,2,4]
# Explanation:
# The above figure represents the given linked list.
# For n = 4, node 2 with value 3 is the middle node, which is marked in red.

# Example 3:
# Input: head = [2,1]
# Output: [2]
# Explanation:
# The above figure represents the given linked list.
# For n = 2, node 1 with value 1 is the middle node, which is marked in red.
# Node 0 with value 2 is the only node remaining after removing node 1.


# Constraints:

# The number of nodes in the list is in the range [1, 10^5].
# 1 <= Node.val <= 10^5

# Brute
# T.C. - O(N)+O(N)
# S.C  - O(1)

# Intuition
# Find length of linked list
# Just stop at the index before the midpoint
# then change links and delete mid node


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        n = 0

        while ptr:
            ptr = ptr.next
            n += 1

        node_idx_to_stop = n // 2
        if node_idx_to_stop == 0:
            return head.next

        ptr = head
        while node_idx_to_stop != 1:
            ptr = ptr.next
            node_idx_to_stop -= 1

        if ptr and ptr.next:
            ptr.next = ptr.next.next

        return head


# Optimal
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# Just do hares floyd and tortoies algos Intuition
# just keep track of also a slow prev as we want
# to stop just at the node before the deleted node

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        slow_prev = head
        while fast and fast.next:
            slow_prev = slow
            slow = slow.next
            fast = fast.next.next

        if slow_prev and slow_prev.next:
            slow_prev.next = slow_prev.next.next
        else:
            return None

        return head
