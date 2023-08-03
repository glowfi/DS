# https://leetcode.com/problems/palindrome-linked-list/ , Medium


# Brute
# T.C. -> O(n) + O(n/2)
# S.C. -> O(n)


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ls = []
        ptr = head

        while ptr:
            ls.append(ptr.val)
            ptr = ptr.next

        n = len(ls)

        for i in range(len(ls)):
            if ls[n - i - 1] != ls[i]:
                return False
        return True


# Optimal
# T.C. -> O(n/2)+O(n/2)+O(n/2)
# S.C. -> O(1)


class Solution:
    def getMid(self, head):
        slow, fast = head, head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # Handle Odd length case , Move the pointer by one as mid element do not require checking
        if fast is not None and fast.next is None:
            slow = slow.next

        return slow

    def rev(self, head):
        prev = None
        ptr = head

        while ptr:
            nx = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = nx

        return prev

    def compare(self, a, b):
        while a is not None and b is not None:
            if a.val != b.val:
                return False

            a = a.next
            b = b.next

        return True

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Find the Middle
        mid = self.getMid(head)

        # Reverse the list
        slow = self.rev(mid)

        # Compare
        result = self.compare(slow, head)

        return result
