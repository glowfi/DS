# https://leetcode.com/problems/sort-list/ , Medium, MergeSort

# Question
# Given the head of a linked list, return the list after sorting it in ascending order.


# Example 1:


# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
# Example 2:


# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]
# Example 3:

# Input: head = []
# Output: []


# Constraints:

# The number of nodes in the list is in the range [0, 5 * 10^4].
# -10^5 <= Node.val <= 10^5


# Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

# Optimal
# T.C. - O(Nlog(N))
# S.C  - O(1)

# Intuition
# Use Merge Sort Algorithm
# Partitioning is done using the getMid function


class Solution:
    def getMid(self, head):
        prev_slow = None
        slow, fast = head, head

        while fast and fast.next:
            prev_slow = slow
            fast = fast.next.next
            slow = slow.next

        return prev_slow

    def mergeSort(self, head):
        # We are at single node
        if head is None or head.next is None:
            return head

        # Cut links only 2 parts from head to mid
        # mid+1 to tail
        mid = self.getMid(head)
        tmp = mid.next
        mid.next = None
        mid = tmp

        left = self.mergeSort(head)
        right = self.mergeSort(mid)
        return self.merge(left, right)

    def merge(self, l1, l2):
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

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.mergeSort(head)
