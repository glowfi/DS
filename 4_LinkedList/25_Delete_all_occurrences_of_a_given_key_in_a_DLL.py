#  https://www.codingninjas.com/studio/problems/delete-all-occurrences-of-a-given-key-in-a-doubly-linked-list_8160461 , Medium

# Optimal
# T.C. -> O(n)
# S.C. -> O(1)


def deleteAllOccurrences(head: Node, k: int) -> Node:
    # No head
    if head is None:
        return head

    # To take care of head node
    dummy = Node(-1)
    dummy.next = head
    head.prev = dummy

    ptr = dummy
    cp = dummy

    while ptr:
        if ptr.data == k:
            ptr.prev.next = ptr.next
            # To take care of tail node
            if ptr.next:
                ptr.next.prev = ptr.prev

        ptr = ptr.next

    return cp.next
