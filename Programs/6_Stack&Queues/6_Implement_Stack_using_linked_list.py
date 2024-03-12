# https://www.geeksforgeeks.org/problems/implement-stack-using-linked-list/1 , Easy


# Optimal
# T.C. - O(1) [push] , O(1) [pop]
# S.C  - O(n)


class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyStack:

    def __init__(self) -> None:
        self.head = None

    def push(self, data):
        tmp = StackNode(data)
        tmp.next = self.head
        self.head = tmp

    def pop(self):
        if self.head is None:
            return -1

        else:
            data = self.head.data
            self.head = self.head.next
            return data
