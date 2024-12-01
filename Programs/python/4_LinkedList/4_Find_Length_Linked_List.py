# https://www.codingninjas.com/studio/problems/count-nodes-of-linked-list_5884,Easy

# Optimal
# T.C. -> O(1)
# S.C. -> O(1)


def length(head):
    _len = 0
    ptr = head

    while ptr:
        ptr = ptr.next
        _len += 1

    return _len
