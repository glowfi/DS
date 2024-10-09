# https://leetcode.com/problems/min-stack/ , Medium


# Brute
# T.C. - O(1) [push],O(1) [pop],O(1) [top],O(1) [getMin]
# S.C  - O(n) [stack] + O(n) [hashmap]


class MinStack:

    def __init__(self):
        self.stk = []
        self.minMap = {}

    def push(self, val: int) -> None:
        currIdx = len(self.stk) - 1
        if currIdx == -1:
            self.minMap[0] = val
        else:
            self.minMap[currIdx + 1] = min(val, self.minMap[currIdx])

        self.stk.append(val)

    def pop(self) -> None:
        if len(self.stk) > 0:
            self.stk.pop(-1)

    def top(self) -> int:
        if len(self.stk) <= 0:
            return -1
        return self.stk[-1]

    def getMin(self) -> int:
        if len(self.stk) <= 0:
            return -1
        lastIdx = len(self.stk) - 1
        return self.minMap[lastIdx]


# Brute
# T.C. - O(1) [push],O(1) [pop],O(1) [top],O(1) [getMin]
# S.C  - O(n) [stack]


class MinStack:

    def __init__(self):
        self.stk: list[int] = []
        self.prevMin = float("inf")

    def push(self, val: int) -> None:
        if len(self.stk) == 0:
            self.prevMin = val
            self.stk.append(val)
        else:
            if val < self.prevMin:
                newVal = 2 * val - self.prevMin
                self.stk.append(newVal)
                self.prevMin = val
            else:
                self.stk.append(val)

    def pop(self) -> None:
        if len(self.stk) > 0:
            top = self.stk.pop(-1)
            if top < self.prevMin:
                self.prevMin = 2 * self.prevMin - top

    def top(self) -> int:
        if len(self.stk) > 0:
            top = self.stk[-1]
            if top < self.prevMin:
                return self.prevMin
            return top
        return -1

    def getMin(self) -> int:
        return self.prevMin
