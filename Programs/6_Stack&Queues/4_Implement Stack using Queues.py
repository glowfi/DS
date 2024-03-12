# https://leetcode.com/problems/implement-queue-using-stacks/ , Easy

# Optimal
# T.C. - [push O(1),pop O(n),peek O(1),empty O(1)]
# S.C  - O(1)


from collections import deque


class MyStack:

    def __init__(self):
        self.q = deque([])

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        for i in range(len(self.q) - 1):
            data = self.q.popleft()
            self.q.append(data)

        return self.q.popleft()

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0
