#  https://www.codingninjas.com/studio/problems/add-one-to-a-number-represented-as-linked-list_920557 , Medium

# Brute
# T.C. -> O(n)+O(n)
# S.C. -> O(n)+O(n)


def addOne(head: Node) -> Node:
    ptr = head
    s = ""

    while ptr:
        s += str(ptr.data)
        ptr = ptr.next

    final = str(int(s) + 1)

    curr = dummy = Node()

    for i in final:
        dummy.next = Node(i)
        dummy = dummy.next

    return curr.next


# Optimal
# T.C. -> O(n)+O(n)+O(n)
# S.C. -> O(n)


def reverseLL(head):
    prev = None
    ptr = head

    while ptr:
        # Save the node's next
        nx = ptr.next

        # Point the node's next to previous node
        ptr.next = prev

        # Update the previoius node as current
        prev = ptr

        # Move to the next node
        ptr = nx

    return prev


def addOne(head: Node) -> Node:
    # write your code here
    carry = 0
    p1, p2 = reverseLL(head), Node(1)

    dummy = curr = Node()

    while p1 and p2:
        # Calculate the sum of current 2 nodes and add any carry from previous node
        currSum = p1.data + p2.data + carry

        # Calcaute the node dataue to be addded
        sm = currSum % 10

        # Create new node
        dummy.next = Node(sm)
        dummy = dummy.next

        # Calculate Carry
        carry = currSum // 10

        p1 = p1.next
        p2 = p2.next

    while p1:
        # Calculate the sum of current 2 nodes and add any carry from previous node
        currSum = p1.data + carry

        # Calcaute the node dataue to be addded
        sm = currSum % 10

        # Create new node
        dummy.next = Node(sm)
        dummy = dummy.next

        # Calculate Carry
        carry = currSum // 10

        p1 = p1.next

    while p2:
        # Calculate the sum of current 2 nodes and add any carry from previous node
        currSum = p2.data + carry

        # Calcaute the node dataue to be addded
        sm = currSum % 10

        # Create new node
        dummy.next = Node(sm)
        dummy = dummy.next

        # Calculate Carry
        carry = currSum // 10

        p2 = p2.next

    if carry:
        # Create new node
        dummy.next = Node(carry)
        dummy = dummy.next

    return reverseLL(curr.next)
