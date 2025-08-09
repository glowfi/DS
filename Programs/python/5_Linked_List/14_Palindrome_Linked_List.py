# https://leetcode.com/problems/palindrome-linked-list , Easy, FloydsAlgo/Observation

# Question
# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

# Example 1:
# Input: head = [1,2,2,1]
# Output: true

# Example 2:
# Input: head = [1,2]
# Output: false


# Constraints:

# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9


# Follow up: Could you do it in O(n) time and O(1) space?

# Brute
# T.C. - O(N)+O(N)
# S.C  - O(N)

# Intuition
# Store the linked list in an array
# check if list is palindromic or not using
# 2 pointer technique


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []

        ptr = head
        while ptr:
            arr.append(ptr.val)
            ptr = ptr.next

        i, j = 0, len(arr) - 1

        while i < j:
            if arr[i] != arr[j]:
                return False

            i += 1
            j -= 1

        return True


# Optimal
# T.C. - O(N)+O(N)+O(N)
# S.C  - O(1)

# Intuition
# Find the middle of linked list
# reverse from the mid to last and get last nodes head
# now keep comparing last node and first node like this


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if fast and not fast.next:  # Handle odd length
            slow = slow.next

        return slow

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

    def checkPalindrome(self, a: ListNode, b: ListNode) -> bool:
        while a and b:
            if a.val != b.val:
                return False

            a = a.next
            b = b.next

        return True

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mid = self.middleNode(head)
        last_node_head = self.reverseList(mid)
        return self.checkPalindrome(head, last_node_head)
