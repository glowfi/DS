# NA , Easy

# Optimal
# T.C. - O(1) [push,pop,top] [We cannot insert elements in the front of the queue even we have some free space left in the front of the queue]
# S.C  - O(cap)


class MyQueue:

    def __init__(self, cap) -> None:
        self.cap = cap
        self.arr = [None] * self.cap
        self.rear = -1
        self.front = -1

    # Function to push an element x in a queue.
    def enqueue(self, x):
        if self.isFull():
            return "Queue is Full!"

        self.rear += 1
        self.arr[self.rear] = x
        return self.printQueue()

    # Function to pop an element from queue and return that element.
    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty!"

        self.front += 1
        removedData = self.arr[self.front]
        return self.printQueue(), f"Removed: {removedData}"

    # Function to get the front element
    def peek(self):
        if not self.isEmpty():
            return self.arr[self.front + 1]
        else:
            return -1

    # Function to get the rear-end element
    def _rear(self):
        if not self.isEmpty():
            return self.arr[self.rear]
        else:
            return -1

    # Function to check queue full
    def isFull(self):
        return self.rear == self.cap - 1

    # Function to check queue empty
    def isEmpty(self):
        return self.front == self.rear

    # Print Queue
    def printQueue(self) -> list[int]:
        ls = []
        for i in range(self.front + 1, self.rear + 1):
            ls.append(self.arr[i])
        return ls


obj = MyQueue(5)
print(obj.enqueue(1))
print(obj.enqueue(2))
print(obj.enqueue(3))
print(obj.enqueue(4))
print(obj._rear())
print(obj.peek())
print(obj.enqueue(5))
print(obj.enqueue(6))
print(obj.dequeue())
print(obj.dequeue())
print(obj.dequeue())
print(obj.dequeue())
print(obj.dequeue())
print(obj.enqueue(6))
print(obj.enqueue(7))
