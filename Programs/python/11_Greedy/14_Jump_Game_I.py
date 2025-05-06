# https://leetcode.com/problems/jump-game/ , Medium


# Recursion
# T.C. - O(N^N)
# S.C  - O(N)

from typing import List


class Solution:
    def solve(self, idx, nums: list[int]) -> bool:
        if idx == len(nums) - 1:
            return True

        if nums[idx] == 0:
            return False

        for i in range(1, nums[idx] + 1):
            if self.solve(i + idx, nums):
                return True

        return False

    def canJump(self, nums: List[int]) -> bool:
        return self.solve(0, nums)


# Memoization
# T.C. - O(N*N)
# S.C  - O(N)+O(N)


class Solution:
    def solve(self, idx, nums: list[int], memo: dict[int, int]) -> bool:
        if idx == len(nums) - 1:
            return True

        if nums[idx] == 0:
            return False

        if idx in memo:
            return memo[idx]

        for i in range(1, nums[idx] + 1):
            if self.solve(i + idx, nums, memo):
                memo[idx] = True
                return True

        memo[idx] = False
        return memo[idx]

    def canJump(self, nums: List[int]) -> bool:
        memo: dict[int, int] = {}
        return self.solve(0, nums, memo)


# Tabulation
# T.C. - O(N*N)
# S.C  - O(N)


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False for _ in range(len(nums))]

        for idx in range(len(nums) - 1, -1, -1):
            if idx == len(nums) - 1:
                dp[idx] = True
                continue

            if nums[idx] == 0:
                dp[idx] = False
                continue

            flag = 0
            for i in range(1, nums[idx] + 1):
                if i < len(nums) and dp[i + idx]:
                    flag = 1
                    break

            if flag == 1:
                dp[idx] = True
                continue

            dp[idx] = False

        return dp[0]


# Space Optimized
# T.C. - O(N)
# S.C  - O(1)

# The key idea is: at every step, track how far you can jump. If your current index
# exceeds your maximum reachable index, you can't move forward—game over.
# I am going to keep track of max index till now
# For every index i am going to touch if this index has been reached by some other index
# If we see that max index till now is less than current index we can say that we
# have not been reached by anyone and return False


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_index = 0

        for i in range(len(nums)):
            if i > max_index:
                return False
            max_index = max(max_index, i + nums[i])

        return True
