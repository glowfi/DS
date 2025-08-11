# https://www.geeksforgeeks.org/problems/find-length-of-loop/1, Easy, FloydsAlgo

# Question
# Given the head of a linked list, determine whether the list contains a loop. If a loop is present,
# return the number of nodes in the loop, otherwise return 0.

# Note: 'c' is the position of the node which is the next pointer of the last node of the linkedlist. If c is 0, then there is no loop.

# Examples:

# Input: head: 1 → 2 → 3 → 4 → 5, c = 2
# Output: 4
# Explanation: There exists a loop in the linked list and the length of the loop is 4.

# Input: head: 25 → 14 → 19 → 33 → 10 → 21 → 39 → 90 → 58 → 45, c = 4
# Output: 7
# Explanation: The loop is from 33 to 45. So length of loop is 33 → 10 → 21 → 39 → 90 → 58 → 45 = 7.
# The number 33 is connected to the last node of the linkedlist to form the loop because according
# to the input the 4th node from the beginning(1 based indexing)
# will be connected to the last node in the LinkedList.

# Input: head: 0 → 1 → 2 → 3, c = 0
# Output: 0
# Explanation: There is no loop.

# Constraints:
# 1 ≤ no. of nodes ≤ 10^6
# 0 ≤ node.data ≤ 10^6
# 0 ≤ c ≤ n-1

# Brute
# T.C. - O(N)
# S.C  - O(N)

# Intuition
# Keep track of index at which we visit node
# moment we find a node we already visit
# return curr_idx-visited_nodes[ptr]


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def countNodesInLoop(self, head: Node):
        visited_nodes: dict[Node, int] = {}

        ptr = head
        curr_idx = 1

        while ptr:
            if ptr in visited_nodes:
                return curr_idx - visited_nodes[ptr]

            visited_nodes[ptr] = curr_idx
            ptr = ptr.next
            curr_idx += 1

        return 0


# Optimal
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# Use hare and floyds algorithm
# after two pointers meet
# we move again until we reach
# slow node again [can be modified for fast too]


class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


class Solution:
    def countNodesInLoop(self, head: Node):
        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                ptr = slow.next
                c = 1
                while ptr != slow:
                    c += 1
                    ptr = ptr.next
                return c

        if not fast or not fast.next:  # No cycle
            return 0
