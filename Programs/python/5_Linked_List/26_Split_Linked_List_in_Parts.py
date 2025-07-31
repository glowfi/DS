# https://leetcode.com/problems/split-linked-list-in-parts , Medium

# Question
# Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

# The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

# The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

# Return an array of the k parts.


# Example 1:
# Input: head = [1,2,3], k = 5
# Output: [[1],[2],[3],[],[]]
# Explanation:
# The first element output[0] has output[0].val = 1, output[0].next = null.
# The last element output[4] is null, but its string representation as a ListNode is [].

# Example 2:
# Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
# Output: [[1,2,3,4],[5,6,7],[8,9,10]]
# Explanation:
# The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.


# Constraints:

# The number of nodes in the list is in the range [0, 1000].
# 0 <= Node.val <= 1000
# 1 <= k <= 50


# Optimal
# T.C. - O(N)+O(K*N)
# S.C  - O(1)

# Intuition
# One thing we know if we have suppose n=10,k=5
# We will have 5 partitions and each parition will
# have atleast 2 nodes right, but suppose we have
# n=10,k=6 then we have 6 partitions and each partitions
# will have atleast 1 node and we are left out with
# 4 extra nodes, we can now assign these node to the
# leftmost partitions as possible


from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        n = 0
        ptr = head

        while ptr:
            ptr = ptr.next
            n += 1

        nodes_in_each_part = n // k
        extra_nodes = n % k

        ans = [None] * k
        ptr = head

        for i in range(k):
            curr_head = ptr
            total_nodes = nodes_in_each_part
            ans[i] = curr_head
            if extra_nodes:
                total_nodes += 1
                extra_nodes -= 1

            # Keep moving current head until we reach the last node
            while curr_head and total_nodes != 1:
                curr_head = curr_head.next
                total_nodes -= 1

            # delete link and move the pointer to head of next partition start
            if curr_head:
                ptr = curr_head.next
                curr_head.next = None
            else:
                curr_head = None

        return ans
