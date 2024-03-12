# NA , Easy

# Optimal
# T.C. - O(1) [push,pop,top] [Unlike normal queue we cant add more elemnts in the front of the queue if there are is any space left]
# S.C  - O(maxCapacity)


class MyCircularQueue:

    def __init__(self, maxCapacity) -> None:
        self.maxCapacity = maxCapacity
        self.arr = [None] * self.maxCapacity
        self.rear = -1
        self.front = -1
        self.currSize = 0

    # Function to push an element x in a queue.
    def enqueue(self, x):
        if self.isFull():
            return "Queue is full!"

        self.arr[(self.rear + 1) % self.maxCapacity] = x
        self.rear += 1
        self.currSize += 1
        return self.arr

    # Function to pop an element from queue and return that element.
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty!"

        self.arr[(self.front + 1) % self.maxCapacity] = None
        self.front += 1
        self.currSize -= 1
        return self.arr

    # Function to get the front element
    def peek(self):
        if not self.isEmpty():
            return self.arr[(self.front + 1) % self.maxCapacity]
        else:
            return -1

    # Function to get the rear-end element
    def _rear(self):
        if not self.isEmpty():
            return self.arr[self.rear % self.maxCapacity]
        else:
            return -1

    # Function to check queue full
    def isFull(self):
        return self.currSize == self.maxCapacity

    # Function to check queue empty
    def isEmpty(self):
        return self.currSize == 0


obj = MyCircularQueue(5)
print(obj.enqueue(1))
print(obj.enqueue(2))
print(obj.enqueue(3))
print(obj.enqueue(4))
print(obj.enqueue(5))
print(obj.enqueue(1))
print(obj.enqueue(6))
print(obj.dequeue())
print(obj.dequeue())
print(obj.enqueue(6))
print(obj.dequeue())
print(obj.dequeue())
print(obj.dequeue())
print(obj.dequeue())
print(obj.dequeue())
print(obj.enqueue(7))
print(obj.enqueue(8))
print(obj.enqueue(8))
print(obj.peek())
print(obj._rear())
