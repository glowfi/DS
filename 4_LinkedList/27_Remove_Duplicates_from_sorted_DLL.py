#  https://www.codingninjas.com/studio/problems/remove-duplicates-from-a-sorted-doubly-linked-list_2420283 , Medium

# Brute
# T.C. -> O(n)+O(nlog(n))+O(n)
# S.C. -> O(n)


def removeDuplicates(head: Node) -> Node:
    st = set()

    ptr = head
    while ptr:
        st.add(ptr.data)
        ptr = ptr.next

    dummy = curr = Node(-1)
    st = list(st)
    st.sort()

    for i in st:
        dummy.next = Node(i, None, dummy)
        dummy = dummy.next

    return curr.next


# Optimal
# T.C. -> O(n)
# S.C. -> O(1)


def removeDuplicates(head: Node) -> Node:
    # No head
    if head is None:
        return head

    # To take care of head node
    dummy = Node(-1)
    dummy.next = head
    head.prev = dummy

    ptr = dummy.next

    while ptr:
        if ptr.prev.data == ptr.data:
            ptr.prev.next = ptr.next
            # To take care of tail node
            if ptr.next:
                ptr.next.prev = ptr.prev

        ptr = ptr.next

    return dummy.next
