#  https://www.codingninjas.com/studio/problems/find-pairs-with-given-sum-in-doubly-linked-list_1164172 , Medium

# Optimal
# T.C. -> O(n)+O(n)
# S.C. -> O(1)


def getEnd(head):
    ptr = head

    while True:
        if ptr.next is None:
            return ptr
        ptr = ptr.next


def findPairs(head: Node, k: int) -> [[int]]:
    start, end = head, getEnd(head)
    ans = []

    # Till they do not meet or start crosses end
    while start != end and end.next != start:
        if start.data + end.data == k:
            ans.append([start.data, end.data])
            start = start.next
            end = end.prev

        elif start.data + end.data > k:
            end = end.prev

        elif start.data + end.data < k:
            start = start.next

    return ans
