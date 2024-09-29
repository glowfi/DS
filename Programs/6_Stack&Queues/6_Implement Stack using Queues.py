# https://leetcode.com/problems/implement-stack-using-queues , Easy

# Optimal
# T.C. - [push O(n),pop O(1),peek O(1),empty O(1)]
# S.C  - O(n)

from collections import deque


class MyStack:

    def __init__(self):
        self.currsize = 0
        self.q = deque([])

    def push(self, x: int) -> None:
        self.q.append(x)
        self.currsize += 1
        for _ in range(self.currsize - 1):
            self.data = self.q.popleft()
            self.q.append(self.data)

    def pop(self) -> int:
        if self.currsize > 0:
            self.currsize -= 1
            return self.q.popleft()
        return -1

    def top(self) -> int:
        if self.currsize > 0:
            return self.q[0]
        return -1

    def empty(self) -> bool:
        return self.currsize == 0
