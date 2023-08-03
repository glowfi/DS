# https://leetcode.com/problems/sort-list/ , Medium

# Brute
# T.C. -> O(n)+Onlog(n)+O(n)
# S.C. -> O(log(n))+O(n)


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        ls = []

        while ptr:
            ls.append(ptr.val)
            ptr = ptr.next

        ls.sort()
        dummy = cp = ListNode()

        for i in range(len(ls)):
            dummy.next = ListNode(ls[i])
            dummy = dummy.next

        return cp.next


# Optimal
# T.C. -> O(nlog(n))
# S.C. -> O(log(n))


class Solution:
    def getMid(self, head):
        start = ListNode(-1)
        start.next = head
        slow, fast = start, start
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def mergeSort(self, head):
        # We are at single node
        if head is None or head.next is None:
            return head

        mid = self.getMid(head)
        tmp = mid.next
        mid.next = None
        mid = tmp

        left = self.mergeSort(head)
        right = self.mergeSort(mid)
        return self.merge(left, right)

    def merge(self, l1, l2):
        d = cp = ListNode()
        while l1 and l2:
            if l1.val <= l2.val:
                d.next = l1
                l1 = l1.next
            else:
                d.next = l2
                l2 = l2.next
            d = d.next

        if l1:
            d.next = l1
        if l2:
            d.next = l2

        return cp.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.mergeSort(head)
