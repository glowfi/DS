# https://leetcode.com/problems/linked-list-cycle, Easy, FloydsAlgo

# Question
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be
# reached again by continuously following the next pointer. Internally, pos is
# used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.


# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

# Example 2:
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

# Example 3:
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.


# Constraints:

# The number of the nodes in the list is in the range [0, 10^4].
# -10^5 <= Node.val <= 10^5
# pos is -1 or a valid index in the linked-list.

# Follow up: Can you solve it using O(1) (i.e. constant) memory?

# Brute
# T.C. - O(N)
# S.C  - O(N)

# Intuition
# Keep track of the nodes as you visit
# if there is a cycle then definitely we will visit a node twice


from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_nodes = set()
        ptr = head

        while ptr:
            if ptr in visited_nodes:
                return True
            visited_nodes.add(ptr)
            ptr = ptr.next

        return False


# Optimal
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# Use floyds hare and tortoise algorithm
# if there is a cycle then hare and tortoise are bound to meet
# at each turn the hare becomes closer to the tortoise by 1 unit
# of distance


from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False
