# https://leetcode.com/problems/intersection-of-two-linked-lists/ , Easy

# Brute
# T.C. -> O(n1)+O(n2)
# S.C. -> O(n1)


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        h = {}
        ptr = headA

        while ptr:
            if ptr not in h:
                h[ptr] = 1
            ptr = ptr.next

        ptr = headB
        while ptr:
            if ptr in h:
                return ptr
            ptr = ptr.next

        return None
