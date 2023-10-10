# https://leetcode.com/problems/linked-list-cycle-ii/ , Medium

# Brute
# T.C. -> O(n)
# S.C. -> O(n)


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        h = {}

        while ptr:
            # Cycle Exists
            if ptr in h:
                return ptr

            if ptr not in h:
                h[ptr] = 1

            ptr = ptr.next

        # No Cycle
        return None


# Optimal
# T.C. -> O(n)
# S.C. -> O(1)


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            # Cycle Exists
            if fast == slow:
                # Take slow pointer to the head
                slow = head

                while fast != slow:
                    fast = fast.next
                    slow = slow.next

                return slow

        # No Cycle
        return None
