# https://leetcode.com/problems/powx-n/ , Medium

# Brute
# T.C. -> O(n)
# S.C. -> O(n) [Recursion stack space]


class Solution:
    def helper(self, x, n):
        if x == 0:
            return 0.0

        if n == 0:
            return 1.0

        return x * self.myPow(x, n - 1)

    def myPow(self, x: float, n: int) -> float:
        val = self.helper(x, abs(n))
        if n > 0:
            return val
        return 1 / val


# Optimal
# T.C. -> O(log(n))
# S.C. -> O(log(n)) [Recursion stack space]


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if x == 0:
                return 0.0

            if n == 0:
                return 1.0

            val = helper(x, n // 2)
            if n % 2 == 0:
                return val * val
            return x * val * val

        val = helper(x, abs(n))
        if n < 0:
            return 1 / val
        return val
