# https://leetcode.com/problems/middle-of-the-linked-list/,Medium

# Brute
# T.C. -> O(n)
# S.C. -> O(1)


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        _len = 0
        ptr = head

        while ptr:
            ptr = ptr.next
            _len += 1

        stop = (_len) // 2
        start = 0
        ptr = head

        while True:
            if start == stop:
                return ptr
            start += 1
            ptr = ptr.next


# Brute
# T.C. -> O(n)
# S.C. -> O(1)


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        # Odd  ->  fast.next is None
        # Even ->  fast is None

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow
