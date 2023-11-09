# https://leetcode.com/problems/count-good-numbers/ , Medium


# Brute
# T.C. - O(n)
# S.C  - P(1)


class Solution:
    def countGoodNumbers(self, n: int) -> int:
        if n == 1:
            return 5

        nodd = n // 2
        neven = n - nodd
        MOD = (10**9) + 7

        toteven = 5**neven
        totodd = 4**nodd

        return ((toteven % MOD) * (totodd % MOD)) % MOD


# Optimal
# T.C. - O(log(n))
# S.C  - P(log(n))


class Solution:
    def getval(self, x, n):
        if n == 0:
            return 1

        val = self.getval(x, n // 2)
        MOD = (10**9) + 7

        if n % 2 != 0:
            return (val * val * x) % MOD
        return (val * val) % MOD

    def countGoodNumbers(self, n: int) -> int:
        if n == 1:
            return 5

        nodd = n // 2
        neven = n - nodd
        MOD = (10**9) + 7

        toteven = self.getval(5, neven)
        totodd = self.getval(4, nodd)

        return ((toteven % MOD) * (totodd % MOD)) % MOD
