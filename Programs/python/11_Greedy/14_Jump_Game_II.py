# https://leetcode.com/problems/jump-game-ii , Medium

# Recursion
# T.C. - O(N^N)
# S.C  - O(N)


from typing import List


class Solution:
    def solve(self, idx, nums: list[int]) -> int:
        if idx >= len(nums) - 1:
            return 0

        if nums[idx] == 0:
            return float("inf")

        mn_steps = float("inf")
        for i in range(1, nums[idx] + 1):
            steps = 1 + self.solve(i + idx, nums)
            mn_steps = min(mn_steps, steps)

        return mn_steps

    def jump(self, nums: List[int]) -> int:
        return self.solve(0, nums)


# Memoization
# T.C. - O(N^2)
# S.C  - O(N)+O(N)

from typing import List


class Solution:
    def solve(self, idx, nums: list[int], memo: dict[int, int]) -> int:
        if idx >= len(nums) - 1:
            return 0

        if nums[idx] == 0:
            return float("inf")

        if idx in memo:
            return memo[idx]

        mn_steps = float("inf")
        for i in range(1, nums[idx] + 1):
            steps = 1 + self.solve(i + idx, nums, memo)
            mn_steps = min(mn_steps, steps)
            memo[idx] = mn_steps

        memo[idx] = mn_steps
        return memo[idx]

    def jump(self, nums: List[int]) -> int:
        memo: dict[int, int] = {}
        return self.solve(0, nums, memo)


# Tabulation
# T.C. - O(N^2)
# S.C  - O(N)

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float("inf") for _ in range(len(nums))]
        dp[len(nums) - 1] = 0

        for idx in range(len(nums) - 2, -1, -1):
            mn_steps = float("inf")
            for i in range(1, nums[idx] + 1):
                if i + idx < len(nums):
                    steps = 1 + dp[i + idx]
                    mn_steps = min(mn_steps, steps)
                    dp[idx] = mn_steps

            dp[idx] = mn_steps

        return dp[0]


# Space Optimized
# T.C. -
# S.C  -
