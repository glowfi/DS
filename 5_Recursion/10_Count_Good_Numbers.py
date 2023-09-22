# https://leetcode.com/problems/count-good-numbers/ , Medium

# Optimal
# T.C. -> O(log(n))
# S.C. -> O(log(n)) [Recursion stack]


class Solution:
    def myPow(self, x: int, n: int, MOD) -> int:
        def helper(x, n):
            if x == 0:
                return 0

            if n == 0:
                return 1

            val = helper(x, n // 2)
            if n % 2 == 0:
                return (val * val) % MOD
            return (x * val * val) % MOD

        val = helper(x, abs(n))
        return val

    def countGoodNumbers(self, n: int) -> int:
        totalOdd = n // 2
        totalEven = n - totalOdd
        MOD = (10**9) + 7

        return (
            self.myPow(5, totalEven, MOD) % MOD * self.myPow(4, totalOdd, MOD) % MOD
        ) % MOD
