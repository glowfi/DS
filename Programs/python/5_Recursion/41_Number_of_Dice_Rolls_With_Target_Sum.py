# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum , Medium

# Recursive Tree
# https://0x0.st/Htdi.520.png

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

        count = 0
        MOD = (10**9) + 7

        for num in range(1, min(target, k) + 1):
            val = self.numRollsToTarget(n - 1, k, target - num)
            count += val % MOD

        return count % MOD
