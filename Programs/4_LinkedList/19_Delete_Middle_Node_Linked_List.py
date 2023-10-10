# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/ , Medium


# Brute
# T.C. -> O(n)
# S.C. -> O(1)


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        ptr = head

        while ptr:
            length += 1
            ptr = ptr.next

        indexToBeDeleted = length // 2
        if indexToBeDeleted == 0:
            return head.next

        ptr = head
        idx = 0

        while ptr:
            if idx == indexToBeDeleted - 1:
                ptr.next = ptr.next.next
                break
            ptr = ptr.next
            idx += 1

        return head


# Optimal
# T.C. -> O(n)
# S.C. -> O(n)


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head

        fast, slow = dummy, dummy

        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next
