# NA , Easy

# Optimal
# T.C. - O(1) [push,pop,top] [Unlike normal queue we cant add more elemnts in the front of the queue if there are is any space left]
# S.C  - O(maxCapacity)


class CQueue:
    def __init__(self, size):
        self.maxCapacity = size
        self.queue = [None for _ in range(size)]
        self.start, self.end = -1, -1
        self.currsize = 0

    def enqueue(self, x):
        if self.size() == self.maxCapacity:
            return
        if self.start == -1 and self.start == -1:
            self.start, self.end = 0, 0
        else:
            self.end = (self.end + 1) % self.maxCapacity

        self.queue[self.end] = x
        self.currsize += 1

    def dequeue(self):
        if self.size() == 0:
            return -1

        x = self.queue[self.start]
        if self.currsize == 1:
            self.start, self.end = -1, -1
        else:
            self.start = (self.start + 1) % self.maxCapacity
        self.currsize -= 1
        return x

    def top(self):
        if self.size() > 0:
            return self.queue[self.start]
        return -1

    def size(self):
        return self.currsize


obj = CQueue(5)

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
print(obj.queue)
print(obj.top())
obj.dequeue()
obj.dequeue()
print(obj.top())
