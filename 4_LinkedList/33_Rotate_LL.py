#  https://leetcode.com/problems/rotate-list/ , Medium


# Brute
# T.C. -> O(n*k)
# S.C. -> O(1)


class Solution:
    def rotateByOne(self, head):
        ptr = cp = head
        prev = ptr

        while True:
            if ptr.next is None:
                save = prev.next
                save.next = cp
                prev.next = None
                return save

            prev = ptr
            ptr = ptr.next

    def getLen(self, head):
        c = 0
        ptr = head

        while ptr:
            c += 1
            ptr = ptr.next
        return c

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or head is None:
            return head

        k = k % self.getLen(head)

        for i in range(k):
            head = self.rotateByOne(head)
        return head


# Optimal
# T.C. -> O(n)+O(n)
# S.C. -> O(1)


class Solution:
    def getLen(self, head):
        c = 0
        ptr = head

        while True:
            if ptr.next is None:
                return [c + 1, ptr]
            c += 1
            ptr = ptr.next

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k == 0:
            return head

        ret = self.getLen(head)
        length = ret[0]
        lastNode = ret[1]
        k = k % length

        if k == 0:
            return head

        movePlaces = length - k
        ptr = head
        c = 1
        save = None

        while True:
            if c == movePlaces:
                save = ptr.next
                ptr.next = None
                break
            c += 1
            ptr = ptr.next

        lastNode.next = head
        return save
