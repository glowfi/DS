# https://www.codingninjas.com/studio/problems/sort-linked-list-of-0s-1s-2s_1071937 , Medium

# Brute
# T.C. -> O(nlog(n))
# S.C. -> O(log(n))


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def getMid(head):
    start = Node(-1)
    start.next = head
    slow, fast = start, start
    while fast.next is not None and fast.next.next is not None:
        fast = fast.next.next
        slow = slow.next
    return slow


def mergeSort(head):
    # We are at single node
    if head is None or head.next is None:
        return head

    mid = getMid(head)
    tmp = mid.next
    mid.next = None
    mid = tmp

    left = mergeSort(head)
    right = mergeSort(mid)
    return merge(left, right)


def merge(l1, l2):
    d = cp = Node(-1)
    while l1 and l2:
        if l1.data <= l2.data:
            d.next = l1
            l1 = l1.next
        else:
            d.next = l2
            l2 = l2.next
        d = d.next

    if l1:
        d.next = l1
    if l2:
        d.next = l2

    return cp.next


def sortList(head):
    return mergeSort(head)


# Optimal
# T.C. -> O(n)
# S.C. -> O(n)


class Node:
    def __init__(self, data=-1):
        self.data = data
        self.next = None


def sortList(head):
    zero = Node()
    one = Node()
    two = Node()

    cp1 = zero
    cp2 = one
    cp3 = two

    ptr = head

    while ptr:
        if ptr.data == 0:
            zero.next = Node(ptr.data)
            zero = zero.next
        elif ptr.data == 1:
            one.next = Node(ptr.data)
            one = one.next
        elif ptr.data == 2:
            two.next = Node(ptr.data)
            two = two.next
        ptr = ptr.next

    zero.next = cp2.next
    one.next = cp3.next
    two.next = None

    return cp1.next


# Optimal
# T.C. -> O(n)+O(n)
# S.C. -> O(3)


def sortList(head):
    cnt = [0] * 3

    ptr = head
    while ptr:
        cnt[ptr.data] += 1
        ptr = ptr.next

    ptr = head
    for i in range(len(cnt)):
        j = 0
        while j < cnt[i]:
            ptr.data = i
            ptr = ptr.next
            j += 1

    return head
