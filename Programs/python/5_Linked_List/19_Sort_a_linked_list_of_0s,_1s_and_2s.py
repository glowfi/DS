# https://www.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1 , Medium, CountSort

# Question
# Given the head of a linked list where nodes can contain values 0s, 1s, and 2s only. Your task is to rearrange the list so that all 0s appear at the beginning, followed by all 1s, and all 2s are placed at the end.

# Examples:

# Input: head = 1 → 2 → 2 → 1 → 2 → 0 → 2 → 2

# Output: 0 → 1 → 1 → 2 → 2 → 2 → 2 → 2

# Explanation: All the 0s are segregated to the left end of the linked list, 2s to the right end of the list, and 1s in between.
# Input: head = 2 → 2 → 0 → 1

# Output: 0 → 1 → 2 → 2

# Explanation: After arranging all the 0s, 1s and 2s in the given format, the output will be 0 → 1 → 2 → 2.
# Constraints:
# 1 ≤ no. of nodes ≤ 10^6
# 0 ≤ node->data ≤ 2


# Optimal
# T.C. - O(N)+O(N)
# S.C  - O(1)

# Intuition
# Use count sort


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def segregate(self, head: Node) -> Node:
        cnt0, cnt1, cnt2 = 0, 0, 0
        ptr = head

        while ptr:
            if ptr.data == 0:
                cnt0 += 1
            if ptr.data == 1:
                cnt1 += 1
            if ptr.data == 2:
                cnt2 += 1
            ptr = ptr.next

        ptr = head
        for _ in range(cnt0):
            ptr.data = 0
            ptr = ptr.next

        for _ in range(cnt1):
            ptr.data = 1
            ptr = ptr.next

        for _ in range(cnt2):
            ptr.data = 2
            ptr = ptr.next

        return head
