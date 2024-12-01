# https://www.geeksforgeeks.org/problems/implement-stack-using-linked-list/1 , Easy


# Optimal
# T.C. - O(1) [push] , O(1) [pop] , O(1) [size] , O(1) [top]
# S.C  - O(n)


class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyStack:

    def __init__(self) -> None:
        self.top = None
        self.currsize = 0

    # Function to push an integer into the stack.
    def push(self, data):
        newnode = StackNode(data)
        newnode.next = self.top
        self.top = newnode
        self.currsize += 1

    # Function to remove an item from top of the stack.
    def pop(self):
        if self.currsize > 0:
            data = self.top.data
            new_top = self.top.next
            self.top = new_top
            self.currsize -= 1
            return data
        return -1

    # Function to get the topmost element
    def peek(self):
        if self.currsize > 0:
            return self.top.data

    # Function to get the size of the stack
    def size(self):
        return self.currsize
