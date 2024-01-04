# https://leetcode.com/problems/climbing-stairs/ , Easy


# Recursion
# T.C. - O(2^n)
# S.C  - O(n)


class Solution:
    def solve(self, n):
        if n == 0:
            return 1

        c = 0

        for i in range(1, 2 + 1):
            if n - i >= 0:
                c += self.solve(n - i)

        return c

    def climbStairs(self, n: int) -> int:
        return self.solve(n)


# Memoization
# T.C. - O(n)
# S.C  - O(n)+O(n)


class Solution:
    def solve(self, n, dp):
        if n == 0:
            return 1

        if n in dp:
            return dp[n]

        c = 0

        for i in range(1, 2 + 1):
            if n - i >= 0:
                c += self.solve(n - i, dp)

        dp[n] = c

        return dp[n]

    def climbStairs(self, n: int) -> int:
        dp = {}
        return self.solve(n, dp)


# Tabulation
# T.C. - O(n)
# S.C  - O(n)


class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {i: 0 for i in range(n + 1)}
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


# Space Optimized
# T.C. - O(n)
# S.C  - O(1)


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        prev_prev = 1
        prev = 1

        for i in range(2, n + 1):
            curr = prev + prev_prev
            prev_prev = prev
            prev = curr

        return prev
