# https://leetcode.com/problems/fibonacci-number/ , Easy

# Brute
# T.C. - O(2^n)
# S.C  - O(n)


class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        last = self.fib(n - 1)
        slast = self.fib(n - 2)

        return last + slast
