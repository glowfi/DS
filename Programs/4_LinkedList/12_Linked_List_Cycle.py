# https://leetcode.com/problems/linked-list-cycle/,Easy

# Brute
# T.C. -> O(n)
# S.C. -> O(n)


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ptr = head
        h = {}

        while ptr:
            if ptr in h:
                return True

            if ptr not in h:
                h[ptr] = 1

            ptr = ptr.next

        return False


# Optimal
# T.C. -> O(n)
# S.C. -> O(1)


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

            # Cycle Exists
            if fast == slow:
                return True

        # No cycle exists
        return False
