# https://www.geeksforgeeks.org/problems/flattening-a-linked-list/1 , Medium, MergeSort

# Question
# Given a linked list containing n head nodes where every node in the linked list contains two pointers:
# (i) next points to the next node in the list.
# (ii) bottom pointer to a sub-linked list where the current node is the head.
# Each of the sub-linked lists nodes and the head nodes are sorted in ascending order based on their data.
# Your task is to flatten the linked list such that all the nodes appear in a single level while maintaining the sorted order.

# Note:
# 1. ↓ represents the bottom pointer and -> represents the next pointer.
# 2. The flattened list will be printed using the bottom pointer instead of the next pointer.

# Examples:

# Input:

# Output: 5-> 7-> 8-> 10 -> 19-> 20-> 22-> 28-> 30-> 35-> 40-> 45-> 50.
# Explanation:
# Bottom pointer of 5 is pointing to 7.
# Bottom pointer of 7 is pointing to 8.
# Bottom pointer of 8 is pointing to 10 and so on.

# Input:

# Output: 5-> 7-> 8-> 10-> 19-> 22-> 28-> 30-> 50
# Explanation:
# Bottom pointer of 5 is pointing to 7.
# Bottom pointer of 7 is pointing to 8.
# Bottom pointer of 8 is pointing to 10 and so on.

# Constraints:
# 0 <= n <= 100
# 1 <= number of nodes in sub-linked list(mi) <= 50
# 1 <= node->data <= 10^4


# Optimal
# T.C. - O(N)
# S.C  - O(N)

# Intuition


class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
        self.bottom = None


class Solution:
    def merge_2_sorted_list(self, head1: Node, head2: Node) -> Node:
        p1, p2 = head1, head2
        tmp = Node(-1)
        cp = tmp

        while p1 and p2:
            if p1.data <= p2.data:
                tmp.bottom = p1
                p1 = p1.bottom
            else:
                tmp.bottom = p2
                p2 = p2.bottom

            tmp = tmp.bottom

        if p1:
            tmp.bottom = p1

        if p2:
            tmp.bottom = p2

        return cp.bottom

    def flatten(self, root):
        flattened_head = None
        ptr = root

        while ptr:
            flattened_head = self.merge_2_sorted_list(flattened_head, ptr)
            ptr = ptr.next

        return flattened_head
