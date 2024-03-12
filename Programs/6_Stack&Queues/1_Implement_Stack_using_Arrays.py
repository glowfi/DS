# NA , Easy


# Optimal
# T.C. - O(1) [push,pop,peek]
# S.C  - O(cap)


class MyStack:

    def __init__(self, cap):
        self.capacity = cap
        self.arr = [None] * self.capacity
        self.top = -1

    # Function to push an integer into the stack.
    def push(self, data):
        if self.isFull():
            return "Stack is Full!"

        self.top += 1
        self.arr[self.top] = data
        return self.printStack()

    # Function to remove an item from top of the stack.
    def pop(self):
        if self.isEmpty():
            return "Stack is Empty!"
        else:
            removedData = self.arr[self.top]
            self.top -= 1
            return self.printStack(), f"Removed: {removedData}"

    # Check Stack Empty
    def isEmpty(self) -> bool:
        return self.top == -1

    # Check Stack Full
    def isFull(self) -> bool:
        return self.top == len(self.arr) - 1

    # Get Stack top element
    def peek(self) -> int:
        if self.top != -1:
            return self.arr[self.top]
        else:
            return -1

    def printStack(self) -> list[int]:
        ls = []
        for i in range(0, self.top + 1):
            ls.append(self.arr[i])
        return ls


obj = MyStack(5)
print(obj.push(1))
print(obj.push(2))
print(obj.push(3))
print(obj.pop())
print(obj.pop())
print(obj.push(4))
print(obj.push(4))
print(obj.push(4))
print(obj.push(4))
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.push(4))
print(obj.push(6))
print(obj.push(7))
print(obj.peek())
