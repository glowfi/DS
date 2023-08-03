# https://leetcode.com/problems/odd-even-linked-list/ , Medium


# Brute
# T.C. -> O(n)+O(n)
# S.C. -> O(n)


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = []
        even = []

        ptr = head
        idx = 1

        while ptr:
            if idx % 2 == 0:
                even.append(ptr.val)
            else:
                odd.append(ptr.val)
            ptr = ptr.next
            idx += 1

        new = ListNode(-1)
        tmp = new

        for i in range(len(odd)):
            new.next = ListNode(odd[i])
            new = new.next

        for j in range(len(even)):
            new.next = ListNode(even[j])
            new = new.next

        return tmp.next


# Optimal
# T.C. -> O(n)
# S.C. -> O(1)


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        odd = None
        even = None

        o, e = None, None

        ptr = head
        idx = 1

        while ptr:
            if idx % 2 != 0:
                # If odd head is not initialized
                if odd is None:
                    odd = ptr
                    o = ptr
                else:
                    o.next = ptr
                    o = o.next
            else:
                # If even head is not initialized
                if even is None:
                    even = ptr
                    e = ptr
                else:
                    e.next = ptr
                    e = e.next

            ptr = ptr.next
            idx += 1

        o.next = even
        e.next = None

        return odd
