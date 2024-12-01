# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/ , Medium


# Brute
# T.C. -> O(n)+O(n)
# S.C. -> O(1)


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        ptr = head

        while ptr:
            length += 1
            ptr = ptr.next

        toBeDeletedIndex = length - n

        # If index comes out to be head (0)
        if toBeDeletedIndex == 0:
            return head.next

        ptr = head
        idx = 0

        while ptr:
            if idx == toBeDeletedIndex - 1:
                ptr.next = ptr.next.next
                break
            ptr = ptr.next
            idx += 1

        return head


# Optimal
# T.C. -> O(n)
# S.C. -> O(n)


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = ListNode(-1)
        start.next = head
        fast, slow = start, start

        for i in range(n):
            fast = fast.next

        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return start.next
