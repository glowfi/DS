#  https://leetcode.com/problems/reverse-nodes-in-k-group/, Hard


# Better
# T.C. -> O(n)
# S.C. -> O(n/k)


class Solution:
    def reverseLL(self, start, end):
        prev = None

        while start != end:
            nx = start.next
            start.next = prev
            prev = start
            start = nx

        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 1:
            return head

        start = end = head

        c = 1
        while end:
            if c == k:
                break

            c += 1
            end = end.next

            if end is None:
                return head

        save1 = end.next
        save2 = end.next

        newHead = self.reverseLL(start, save1)
        start.next = self.reverseKGroup(save2, k)
        return newHead


# Optimal
# T.C. -> O(n)
# S.C. -> O(1)


class Solution:
    def reverseLL(self, start, end):
        prev = None

        while start != end:
            nx = start.next
            start.next = prev
            prev = start
            start = nx

        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 1:
            return head

        start = end = head
