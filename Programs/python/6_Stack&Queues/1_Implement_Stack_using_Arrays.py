# NA , Easy


# Optimal
# T.C. - O(1) [push,pop,peek,size]
# S.C  - O(maxCapacity)


class Stack:
    def __init__(self, size):
        self.maxCapacity = size
        self.stack = [None for _ in range(size)]
        self.top = -1

    def push(self, x):
        if self.size() >= self.maxCapacity:
            return
        self.top += 1
        self.stack[self.top] = x

    def pop(self):
        if self.size() == 0:
            return -1

        x = self.stack[self.top]
        self.top -= 1
        return x

    def peek(self):
        if self.size() > 0:
            return self.stack[self.top]
        return -1

    def size(self):
        return self.top + 1

    def printStack(self):
        print(self.stack)


obj = Stack(5)
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.push(5)
obj.push(6)
print(obj.peek())
obj.printStack()
obj.pop()
obj.pop()
obj.pop()
obj.pop()
obj.pop()
print(obj.peek())
