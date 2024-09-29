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
        self.start, self.end = None, None
        self.currsize = 0

    # Function to push an element into the queue.
    def push(self, item):
        newnode = Node(item)
        if self.size() == 0:
            self.start, self.end = newnode, newnode
        else:
            self.end.next = newnode
            self.end = newnode
        self.currsize += 1

    # Function to pop front element from the queue.
    def pop(self):
        if self.size() > 0:
            data = self.start.data
            currStart = self.start
            newStart = self.start.next
            currStart.next = None
            self.start = newStart
            self.currsize -= 1
            return data
        return -1

    # Function to get the topmost element
    def peek(self):
        if self.size() > 0:
            return self.start.data

    # Function to get the size of the stack
    def size(self):
        return self.currsize
