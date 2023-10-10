# https://www.codingninjas.com/studio/problems/find-length-of-loop_8160455 , Medium


# Brute
# T.C. -> O(n)
# S.C. -> O(n)


def lengthOfLoop(head: Node) -> int:
    h = {}
    ptr = head
    c = 1

    while ptr:
        if ptr not in h:
            h[ptr] = c

        # Cycle Exists
        if ptr.next in h:
            return (c + 1) - h[ptr.next]

        ptr = ptr.next
        c += 1

    # No Cycle
    return 0


# Optimal
# T.C. -> O(n)
# S.C. -> O(1)


def lengthOfLoop(head: Node) -> int:
    slow, fast = head, head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        # Cycle Exists
        if fast == slow:
            length = 1
            slow = slow.next
            while slow != fast:
                slow = slow.next
                length += 1
            return length

    # No Cycle Exist
    return 0
