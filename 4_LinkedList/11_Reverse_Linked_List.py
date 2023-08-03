# https://leetcode.com/problems/reverse-linked-list/,Easy

# Optimal (Iterative)
# T.C. -> O(n)
# S.C. -> O(1)


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        ptr = head

        while ptr:
            # Save Next Reference
            nx = ptr.next

            # Next will point to prev
            ptr.next = prev

            # Save current reference as it is going to be next of next node
            prev = ptr

            # go to next node
            ptr = nx

        return prev


# Optimal (Recursive)
# T.C. -> O(n)
# S.C. -> O(1)


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rev(prev, curr):
            if curr is None:
                return prev

            nx = curr.next
            curr.next = prev
            prev = curr
            return rev(prev, nx)

        return rev(None, head)
