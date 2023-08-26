# https://leetcode.com/problems/merge-two-sorted-lists/ , Easy


# Optimal
# T.C. -> O(n1+n2)
# S.C. -> O(n1+n2)


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        p1, p2 = list1, list2
        curr = dummy = ListNode(-1)

        while p1 and p2:
            if p1.val <= p2.val:
                curr.next = p1
                p1 = p1.next
                curr = curr.next
            else:
                curr.next = p2
                p2 = p2.next
                curr = curr.next

        if p1:
            curr.next = p1

        if p2:
            curr.next = p2

        return dummy.next
