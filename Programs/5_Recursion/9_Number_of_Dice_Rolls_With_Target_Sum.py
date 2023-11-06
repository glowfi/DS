# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum , Medium


# Brute [Ans in Body]
# T.C. - O(k ^ n)
# S.C  - O(n)


class Solution:
    @lru_cache(maxsize=None)
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if n == 0:
            if target == 0:
                return 1
            return 0

        c = 0
        MOD = (10**9) + 7
        for i in range(1, min(k, target) + 1):
            c += self.numRollsToTarget(n - 1, k, target - i)

        return c % MOD
