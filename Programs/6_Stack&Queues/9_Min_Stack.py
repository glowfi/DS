# https://leetcode.com/problems/min-stack/ , Medium


# Optimal
# T.C. - O(1) [push],O(1) [pop],O(1) [top],O(1) [getMin]
# S.C  - O(n) [stack] + O(n) [hashmap]

from collections import deque


class MinStack:

    def __init__(self):
        self.stk = deque([])
        self.min_map = {}

    def push(self, val: int) -> None:
        if len(self.stk) == 0:
            self.min_map[0] = val
        else:
            self.min_map[len(self.stk)] = min(val, self.min_map[len(self.stk) - 1])

        self.stk.append(val)

    def pop(self) -> None:
        if not len(self.stk) == 0:
            self.stk.pop()

    def top(self) -> int:
        if len(self.stk) > 0:
            return self.stk[-1]
        return -1

    def getMin(self) -> int:
        return self.min_map[len(self.stk) - 1]
