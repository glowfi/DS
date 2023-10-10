# https://www.codingninjas.com/studio/problems/introduction-to-doubly-linked-list_8160413,Easy

# Brute
# T.C. -> O(n)
# S.C. -> O(1)


def constructDLL(arr: [int]) -> Node:
    head = None

    for i in range(len(arr)):
        if head is None:
            head = Node(arr[i], None, None)
        else:
            ptr = head

            while True:
                if ptr.next is None:
                    break
                ptr = ptr.next
            ptr.next = Node(arr[i], None, ptr)

    return head


# Optimal
# T.C. -> O(n)
# S.C. -> O(1)


def constructDLL(arr: [int]) -> Node:
    dummy = Node()
    curr = dummy

    for i in range(len(arr)):
        dummy.next = Node(arr[i], None, dummy)
        dummy = dummy.next

    return curr.next
