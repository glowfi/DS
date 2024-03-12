# https://leetcode.com/problems/implement-queue-using-stacks/ , Easy

# Optimal
# T.C. - [push O(1),pop O(n),peek O(1),empty O(1)]
# S.C  - O(n)


from collections import deque


class MyQueue:

    def __init__(self):
        self.q = deque([])

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        for i in range(len(self.q) - 1):
            self.q[i], self.q[i + 1] = self.q[i + 1], self.q[i]

        return self.q.pop()

    def peek(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0
