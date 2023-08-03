# https://www.codingninjas.com/studio/problems/insert-at-end-of-doubly-linked-list_8160464,Easy

# Optimal
# T.C. -> O(n)
# S.C. -> O(1)


def insertAtTail(head: Node, k: int) -> Node:
    if head is None:
        return Node(k)

    ptr = head

    while True:
        if ptr.next is None:
            break
        ptr = ptr.next

    ptr.next = Node(k, None, ptr)

    return head
