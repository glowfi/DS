# https://www.codingninjas.com/studio/problems/insert-node-at-the-beginning_8144739,Easy

# Optimal
# T.C. -> O(1)
# S.C. -> O(1)


def insertAtFirst(list: Node, newValue: int) -> Node:
    head = Node(newValue)
    head.next = list
    return head
