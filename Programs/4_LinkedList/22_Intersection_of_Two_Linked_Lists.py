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


# Optimal
# T.C. -> O(n1)+O(n2)+O(n2-n1)+O(n2) [Assuming n2 is largest]
# S.C. -> O(1)


class Solution:
    def getLen(self, head):
        ptr = head
        c = 0
        while ptr:
            ptr = ptr.next
            c += 1
        return c

    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        a, b = self.getLen(headA), self.getLen(headB)

        diff = abs(a - b)
        p1, p2 = headA, headB

        # Determine the greatest among A and B
        if a <= b:
            # Move B diff places
            for i in range(diff):
                p2 = p2.next
        else:
            # Move A diff places
            for i in range(diff):
                p1 = p1.next

        while p1 and p2:
            if p1 == p2:
                return p1
            p1 = p1.next
            p2 = p2.next

        return None
