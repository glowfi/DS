# https://leetcode.com/problems/online-stock-span , Medium


# Optimal [with 2d array]
# T.C. - O(n)
# S.C  - O(n^2)


class StockSpanner:

    def __init__(self):
        self.stk = []
        self.currIdx = 0

    def next(self, price: int) -> int:
        ans = -1
        while self.stk and self.stk[-1][1] <= price:
            self.stk.pop(-1)

        if self.stk:
            ans = self.currIdx - self.stk[-1][0]
        else:
            ans = self.currIdx + 1

        self.stk.append([self.currIdx, price])
        self.currIdx += 1
        return ans


# Optimal [without 2d array]
# T.C. - O(n)
# S.C  - O(n)+O(n)


class StockSpanner:

    def __init__(self):
        self.stk = []
        self.currIdx = 0
        self.arr = []

    def next(self, price: int) -> int:
        ans = 0
        self.arr.append(price)
        while self.stk and self.arr[self.stk[-1]] <= price:
            self.stk.pop(-1)

        if self.stk:
            ans += self.currIdx - self.stk[-1]
        else:
            ans = self.currIdx + 1

        self.stk.append(self.currIdx)

        self.currIdx += 1

        return ans


# Optimal [https://www.geeksforgeeks.org/problems/stock-span-problem-1587115621/1]
# T.C. - O(n)
# S.C  - O(n)


class Solution:
    def calculateSpan(self, a, n):
        stack = []
        out = [0] * n

        for i in range(n):
            while stack and a[stack[-1]] <= a[i]:
                stack.pop(-1)

            if stack:
                # found a break point
                out[i] += i - stack[-1]
            else:
                # all elements were smaller
                out[i] = i + 1

            stack.append(i)

        return out
