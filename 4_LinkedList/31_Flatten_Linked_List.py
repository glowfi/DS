#  https://www.codingninjas.com/studio/problems/flatten-a-linked-list_1112655 , Medium

# Brute
# k-> Total no of nodes
# T.C. -> O(k)+O(klog(k))+O(k)
# S.C. -> O(k)


def flattenLinkedList(head: Node) -> Node:
    ls = []

    ptr = head

    while ptr:
        ls.append(ptr.data)
        tmp = ptr.child

        while tmp:
            ls.append(tmp.data)
            tmp = tmp.child

        ptr = ptr.next

    ls.sort()

    dummy = curr = Node(-1)
    for i in ls:
        dummy.child = Node(i)
        dummy = dummy.child

    return curr.child


# Optimal
# T.C. -> O(n*n*k)
# S.C. -> O(n*k)


def merge2sortedlists(l1, l2):
    p1, p2 = l1, l2
    tmp = curr = Node(-1)

    while p1 and p2:
        if p1.data <= p2.data:
            tmp.child = p1
            p1 = p1.child
            tmp = tmp.child
        else:
            tmp.child = p2
            p2 = p2.child
            tmp = tmp.child

    if p1:
        tmp.child = p1

    if p2:
        tmp.child = p2

    return curr.child


def flattenLinkedList(head: Node) -> Node:
    if head is None or head.next is None:
        return head

    l1 = flattenLinkedList(head.next)
    l2 = head

    return merge2sortedlists(l2, l1)
