# https://www.geeksforgeeks.org/problems/remove-duplicates-from-a-sorted-doubly-linked-list/1, Easy, Task

# Question
# Given a doubly linked list of n nodes sorted by values, the task is to remove duplicate nodes present in the linked list.

# Example 1:

# Input:
# n = 6
# 1<->1<->1<->2<->3<->4
# Output:
# 1<->2<->3<->4
# Explanation:
# Only the first occurance of node with value 1 is
# retained, rest nodes with value = 1 are deleted.
# Example 2:

# Input:
# n = 7
# 1<->2<->2<->3<->3<->4<->4
# Output:
# 1<->2<->3<->4
# Explanation:
# Only the first occurance of nodes with values 2,3 and 4 are
# retained, rest repeating nodes are deleted.
# Your Task:
# You have to complete the method removeDuplicates() which takes 1 argument: the head of the linked list.  Your function should return a pointer to a linked list with no duplicate element.

# Constraint:
# 1 <= n <= 10^5
# Expected Time Complexity: O(n)
# Expected Space Complexity: O(1)


# Optimal
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# if prev nodes value is same as current then delete node


class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None
        self.prev = None


class Solution:
    def removeDuplicates(self, head):
        # Handle edge case where list is empty
        if not head:
            return head

        ptr = head.next

        while ptr:
            savedNxt = ptr.next

            # If the current node's data matches x
            if ptr.data == ptr.prev.data:
                if ptr and ptr.prev:
                    ptr.prev.next = ptr.next

                if ptr and ptr.next:
                    ptr.next.prev = ptr.prev

            ptr = savedNxt

        return head
