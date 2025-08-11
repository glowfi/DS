# https://leetcode.com/problems/merge-k-sorted-lists, Hard, MergeSort

# Question
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.


# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted linked list:
# 1->1->2->3->4->4->5->6
# Example 2:

# Input: lists = []
# Output: []
# Example 3:

# Input: lists = [[]]
# Output: []


# Constraints:

# k == lists.length
# 0 <= k <= 104
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4

# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 10^4.

# Optimal
# T.C. - O(Nlog(N))
# S.C  - O(N)

# Intuition
# Use merge sort algo


from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge2sortedList(self, l1: ListNode, l2: ListNode):
        d = cp = ListNode()
        while l1 and l2:
            if l1.val <= l2.val:
                d.next = l1
                l1 = l1.next
            else:
                d.next = l2
                l2 = l2.next

            d = d.next

        if l1:
            d.next = l1
        if l2:
            d.next = l2

        return cp.next

    def mergeSort(self, lists: list[ListNode], st: int, en: int) -> ListNode:
        if len(lists) == 0:
            return None

        if st == en:
            return lists[st]

        mid = (st + en) // 2

        left = self.mergeSort(lists, st, mid)
        right = self.mergeSort(lists, mid + 1, en)
        return self.merge2sortedList(left, right)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.mergeSort(lists, 0, len(lists) - 1)
