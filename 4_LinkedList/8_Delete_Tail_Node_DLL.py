# https://www.codingninjas.com/studio/problems/delete-last-node-of-a-doubly-linked-list_8160469,Easy

# Optimal
# T.C. -> O(n)
# S.C. -> O(1)


def deleteLastNode(head: Node) -> Node:
    ptr = head

    # Means 1 length DLL
    if ptr.next is None:
        _head = None
        return _head

    while True:
        if ptr.next.next is None:
            break
        ptr = ptr.next

    ptr.next = None

    return head
