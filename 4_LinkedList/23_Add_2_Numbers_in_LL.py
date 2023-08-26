#  https://leetcode.com/problems/add-two-numbers/ , Medium

# Brute
# T.C. -> O(n1)+O(n2)+O(n1)+O(n2)+O(n1+n2)+O(n1+n2) = 4O(n1+n2)
# S.C. -> O(n1+n2)+O(n1+n2)+O(n+n2) = 3O(n1+n2)


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        ptr = l1
        s1 = ""

        while ptr:
            s1 += str(ptr.val)
            ptr = ptr.next

        ptr = l2
        s2 = ""

        while ptr:
            s2 += str(ptr.val)
            ptr = ptr.next

        s1 = int(s1[::-1])
        s2 = int(s2[::-1])
        final = str(s1 + s2)[::-1]

        curr = dummy = ListNode()

        for i in final:
            curr.next = ListNode(int(i))
            curr = curr.next

        return dummy.next


# Optimal
# T.C. -> O(n1+n2)
# S.C. -> O(n1+n2)


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        carry = 0
        p1, p2 = l1, l2

        dummy = curr = ListNode()

        while p1 and p2:
            # Calculate the sum of current 2 nodes and add any carry from previous node
            currSum = p1.val + p2.val + carry

            # Calcaute the node value to be addded
            sm = currSum % 10

            # Create new node
            dummy.next = ListNode(sm)
            dummy = dummy.next

            # Calculate Carry
            carry = currSum // 10

            p1 = p1.next
            p2 = p2.next

        while p1:
            # Calculate the sum of current 2 nodes and add any carry from previous node
            currSum = p1.val + carry

            # Calcaute the node value to be addded
            sm = currSum % 10

            # Create new node
            dummy.next = ListNode(sm)
            dummy = dummy.next

            # Calculate Carry
            carry = currSum // 10

            p1 = p1.next

        while p2:
            # Calculate the sum of current 2 nodes and add any carry from previous node
            currSum = p2.val + carry

            # Calcaute the node value to be addded
            sm = currSum % 10

            # Create new node
            dummy.next = ListNode(sm)
            dummy = dummy.next

            # Calculate Carry
            carry = currSum // 10

            p2 = p2.next

        if carry:
            # Create new node
            dummy.next = ListNode(carry)
            dummy = dummy.next

        return curr.next
