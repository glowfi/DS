# https://www.geeksforgeeks.org/problems/add-1-to-a-number-represented-as-linked-list/1 , Medium

# Question
# You are given a linked list where each element in the list is a node and have an integer data. You need to add 1 to the number formed by concatinating all the list node numbers together and return the head of the modified linked list.

# Note: The head represents the first element of the given array.

# Examples :

# Input: LinkedList: 4->5->6
# Output: 457

# Explanation: 4->5->6 represents 456 and when 1 is added it becomes 457.
# Input: LinkedList: 1->2->3
# Output: 124

# Explanation:  1->2->3 represents 123 and when 1 is added it becomes 124.

# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(1)

# Constraints:
# 1 <= len(list) <= 10^5
# 0 <= list[i] <= 9


# Optimal
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# Reverse linked list
# Add 1
# Reverse linked list and return head


from typing import Optional


class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


class Solution:
    def reverseList(self, head: Optional[Node]) -> Optional[Node]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

    def addTwoNumbers(self, l1: Optional[Node], l2: Optional[Node]) -> Optional[Node]:
        ptr1, ptr2 = l1, l2

        new_head = Node(-1)
        curr = new_head
        carry = 0

        while ptr1 and ptr2:
            sm = ptr1.data + ptr2.data + carry
            carry = sm // 10
            res = sm % 10
            curr.next = Node(res)

            curr = curr.next
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        while ptr1:
            sm = ptr1.data + carry
            carry = sm // 10
            res = sm % 10
            curr.next = Node(res)

            curr = curr.next
            ptr1 = ptr1.next

        while ptr2:
            sm = ptr2.data + carry
            carry = sm // 10
            res = sm % 10
            curr.next = Node(res)

            curr = curr.next
            ptr2 = ptr2.next

        if carry > 0:
            curr.next = Node(carry)

        return new_head.next

    def addOne(self, head: Node):
        head = self.addTwoNumbers(Node(1), self.reverseList(head))
        return self.reverseList(head)
