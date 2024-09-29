# https://leetcode.com/problems/implement-queue-using-stacks/ , Easy

# Optimal
# T.C. - [push O(2n),pop O(1),peek O(1),empty O(1)]
# S.C  - O(n)+O(n)

# [push] [Approach 1 if less number of push operations]
# s1->s2
# x->s1
# s2->s1


class MyQueue:

    def __init__(self):
        self.currsize = 0
        self.s1, self.s2 = [], []

    def push(self, x: int) -> None:
        while len(self.s1):
            self.s2.append(self.s1.pop(-1))

        self.s1.append(x)
        self.currsize += 1

        while len(self.s2):
            self.s1.append(self.s2.pop(-1))

    def pop(self) -> int:
        if self.currsize > 0:
            self.currsize -= 1
            return self.s1.pop(-1)
        return -1

    def peek(self) -> int:
        if self.currsize > 0:
            return self.s1[-1]
        return -1

    def empty(self) -> bool:
        return self.currsize == 0


# [push] [Approach 2 if more number of push operations]
# s1->s2
# x->s1
# s2->s1

# Optimal
# T.C. - [push O(1),pop O(n),peek O(n),empty O(1)]
# S.C  - O(n)+O(n)


class MyQueue:

    def __init__(self):
        self.currsize = 0
        self.s1, self.s2 = [], []

    def push(self, x: int) -> None:
        self.s1.append(x)
        self.currsize += 1

    def pop(self) -> int:
        if len(self.s2) > 0:
            self.currsize -= 1
            return self.s2.pop(-1)
        else:
            while len(self.s1):
                self.s2.append(self.s1.pop(-1))
            self.currsize -= 1
            return self.s2.pop(-1)

    def peek(self) -> int:
        if len(self.s2) > 0:
            return self.s2[-1]
        else:
            while len(self.s1):
                self.s2.append(self.s1.pop(-1))
            return self.s2[-1]

    def empty(self) -> bool:
        return self.currsize == 0
