# https://www.codingninjas.com/studio/problems/search-in-a-linked-list_975381,Easy

# Optimal
# T.C. -> O(n)
# S.C. -> O(1)


def searchInLinkedList(head, k):
    ptr = head
    while ptr:
        if ptr.data == k:
            return 1
        ptr = ptr.next

    return 0
