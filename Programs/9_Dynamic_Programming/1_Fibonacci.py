# https://leetcode.com/problems/fibonacci-number/ , Easy

# Recursion
# T.C. - O(2^n)
# S.C  - O(n)


class Solution:
    def solve(self, n):
        # Base
        if n <= 1:
            return n
        # Hypo
        prev = self.solve(n - 1)
        prev_prev = self.solve(n - 2)

        # Induction
        return prev + prev_prev

    def fib(self, n: int) -> int:
        return self.solve(n)


# Memoization
# T.C. - O(n)
# S.C  - O(n) + O(n)


class Solution:
    def solve(self, n, dp):
        # Base
        if n <= 1:
            return n

        if n in dp:
            return dp[n]

        # Hypo
        prev = self.solve(n - 1, dp)
        prev_prev = self.solve(n - 2, dp)

        dp[n] = prev_prev + prev

        # Induction
        return dp[n]

    def fib(self, n: int) -> int:
        dp = {}
        return self.solve(n, dp)


# Tabulation
# T.C. - O(n)
# S.C  - O(n)


class Solution:
    def fib(self, n: int) -> int:
        dp = {i: 0 for i in range(n + 1)}
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


# Space Optimized
# T.C. - O(n)
# S.C  - O(1)


class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        prev_prev = 0
        prev = 1

        for i in range(2, n + 1):
            curr = prev + prev_prev
            prev_prev = prev
            prev = curr

        return prev
