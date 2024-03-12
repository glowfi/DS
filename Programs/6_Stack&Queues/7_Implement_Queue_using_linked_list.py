# https://www.geeksforgeeks.org/problems/implement-queue-using-linked-list/1 , Easy


# Optimal
# T.C. - O(1) [push] , O(1) [pop]
# S.C  - O(n)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyQueue:
    def __init__(self) -> None:
        self.rear = None
        self.front = None  # head
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def push(self, item):
        newnode = Node(item)

        if self.front is None:
            self.front = newnode
            self.rear = newnode
        else:
            self.rear.next = newnode
            self.rear = newnode
        self.size += 1

    def pop(self):
        if not self.isEmpty():
            data = self.front.data
            self.front = self.front.next
            self.size -= 1
            return data
        return -1
