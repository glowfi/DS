# https://www.geeksforgeeks.org/problems/search-in-linked-list-1664434326/1, Easy, Basic

# Question
# Given a linked list of n nodes and a key, the task is to check if the key is present in the linked list or not.

# Example:

# Input: n = 4, key = 3
# 1->2->3->4
# Output: true
# Explanation: 3 is present in Linked List, so the function returns true.

# Constraint:
# 1 <= n <= 10^5
# 1 <= key <= 10^5


# Optimal
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# Keep traversing the linked list
# if the curr node's val is the key
# val return True
# else if we have reached the end of
# linked list return False


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None


class Solution:
    def searchKey(self, n: int, head: Node, key: int) -> bool:
        ptr = head

        while ptr:
            if ptr.data == key:
                return True
            ptr = ptr.next

        return False
