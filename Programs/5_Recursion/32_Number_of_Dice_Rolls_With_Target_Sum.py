# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum , Medium

# Recursive Tree
# https://0x0.st/Htdi.520.png

# Brute [Ans in Body]
# T.C. - O(k ^ n)
# S.C  - O(n)


class Solution:
    @lru_cache(maxsize=None)
    def helper(self, idx, faces, target, turns) -> int:
        if idx == turns:
            if target == 0:
                return 1
            return 0

        count = 0
        MOD = (10**9) + 7

        for i in range(1, min(faces, target) + 1):
            count += self.helper(idx + 1, faces, target - i, turns)

        return count % MOD

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        return self.helper(0, k, target, n)
