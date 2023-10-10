# https://www.codingninjas.com/studio/problems/introduction-to-linked-list_8144737,Easy

# Brute
# T.C. -> O(n)
# S.C. -> O(1)


def constructLL(arr: [int]) -> Node:
    head = None

    for i in range(len(arr)):
        # No elements inserted yet
        if head is None:
            head = Node(arr[i])
        else:
            ptr = head
            while True:
                if ptr.next is None:
                    break
                ptr = ptr.next
            ptr.next = Node(arr[i])

    return head


# Optimal
# T.C. -> O(n)
# S.C. -> O(1)


def constructLL(arr: [int]) -> Node:
    dummy = Node()
    curr = dummy

    for i in range(len(arr)):
        dummy.next = Node(arr[i])
        dummy = dummy.next

    return curr.next
