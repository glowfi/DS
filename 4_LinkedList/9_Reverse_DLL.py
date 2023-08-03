# https://www.codingninjas.com/studio/problems/reverse-a-doubly-linked-list_1116098,Medium

# Brute
# T.C. -> O(n)+O(n)
# S.C. -> O(n)


class Node:
    def __init__(self, data, next, prev):
        self.data = data
        self.next = next
        self.prev = prev


def reverseDLL(head):
    ptr = head
    ls = []

    while ptr:
        ls.append(ptr.data)
        ptr = ptr.next

    ls[:] = ls[::-1]

    dummy = Node(-1, None, None)
    curr = dummy

    for i in range(len(ls)):
        dummy.next = Node(ls[i], None, dummy)
        dummy = dummy.next

    return curr.next


# Optimal
# T.C. -> O(n)
# S.C. -> O(1)


def reverseDLL(head):
    prev = None
    ptr = head

    while ptr:
        # Save next reference
        saveNxt = ptr.next

        # Prev will point to next
        ptr.prev = saveNxt

        # Next will point to prev
        ptr.next = prev

        # Save prev reference
        prev = ptr

        # Go to next pointer
        ptr = saveNxt

    return prev
