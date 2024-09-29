# NA , Easy

# Optimal
# T.C. - O(1) [enqueue,dequeue,top,size] [We cannot insert elements in the front of the queue even we have some free space left in the front of the queue]
# S.C  - O(maxCapacity)


class Queue:
    def __init__(self, size):
        self.maxCapacity = size
        self.queue = [None for _ in range(size)]
        self.start, self.end = -1, -1
        self.currsize = 0

    def enqueue(self, x):
        if self.end == self.maxCapacity - 1 or self.size() == self.maxCapacity:
            return
        if self.start == -1 and self.start == -1:
            self.start, self.end = 0, 0
        else:
            self.end += 1

        self.queue[self.end] = x
        self.currsize += 1

    def dequeue(self):
        if self.size() == 0:
            return -1

        x = self.queue[self.start]
        self.start += 1
        self.currsize -= 1
        return x

    def top(self):
        if self.size() > 0:
            return self.queue[self.start]
        return -1

    def size(self):
        return self.currsize


obj = Queue(5)

obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
print(obj.top())
obj.enqueue(4)
obj.enqueue(5)
print(obj.top())
obj.dequeue()
obj.dequeue()
obj.dequeue()
print(obj.end, obj.currsize)
obj.enqueue(12)
print(obj.top())
obj.dequeue()
obj.dequeue()
print(obj.top())
