# https://leetcode.com/problems/lru-cache/ ,Medium


# Optimal
# T.C. -> O()
# S.C. -> O()


class Node:
    def __init__(self, data: list[int]):
        self.next: Node | None = None
        self.prev: Node | None = None
        self.data: list[int] = data


class LRUCache:

    def __init__(self, capacity: int):
        self.maxSize: int = capacity
        self.currsize: int = 0
        self.nodesMap: dict[int, Node] = {}
        self.head: Node = Node([-1, -1])
        self.tail: Node = Node([-1, -1])

        self.head.next = self.tail
        self.tail.prev = self.head

    def delete(self, node: Node):
        val = node.data[0]

        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        node.next = None
        node.prev = None

        del self.nodesMap[val]
        self.currsize -= 1

    def get(self, key: int) -> int:
        if key in self.nodesMap:
            node_to_move = self.nodesMap[key]

            if node_to_move.prev:
                node_to_move.prev.next = node_to_move.next
            if node_to_move.next:
                node_to_move.next.prev = node_to_move.prev

            node_to_move.next = None
            node_to_move.prev = None

            nextVal = self.head.next
            self.head.next = node_to_move
            node_to_move.prev = self.head
            node_to_move.next = nextVal
            nextVal.prev = node_to_move

            return node_to_move.data[1]

        return -1

    def insert(self, key: int, value: int):
        newNode = Node([key, value])
        # if inserting for first time
        if self.head.next == self.tail:
            self.head.next = newNode
            newNode.prev = self.head
            newNode.next = self.tail
            self.tail.prev = newNode
        else:
            nextVal = self.head.next
            self.head.next = newNode
            newNode.prev = self.head
            newNode.next = nextVal
            nextVal.prev = newNode

        self.nodesMap[key] = newNode
        self.currsize += 1

    def put(self, key: int, value: int) -> None:
        # if key exists already
        if key in self.nodesMap:
            oldNode = self.nodesMap[key]
            oldNode.data = [key, value]
            self.nodesMap[key] = oldNode
            self.get(key)
            return
        else:
            if self.currsize == self.maxSize:
                # evict node before tail
                self.delete(self.tail.prev)
            self.insert(key, value)
