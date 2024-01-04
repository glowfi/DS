# https://leetcode.com/problems/house-robber/ , Medium

# Recursion
# T.C. - O(2^n)
# S.C  - O(n)


class Solution:
    def solve(self, idx, nums):
        if idx < 0:
            return 0

        if idx == 0:
            return nums[0]

        # Take
        take = self.solve(idx - 2, nums) + nums[idx]

        # notTake
        notTake = self.solve(idx - 1, nums)

        return max(take, notTake)

    def rob(self, nums: List[int]) -> int:
        return self.solve(len(nums) - 1, nums)


# Memoization
# T.C. - O(n)
# S.C  - O(n)+O(n)


class Solution:
    def solve(self, idx, nums, dp):
        if idx < 0:
            return 0

        if idx == 0:
            return nums[0]

        if idx in dp:
            return dp[idx]

        # Take
        take = self.solve(idx - 2, nums, dp) + nums[idx]

        # notTake
        notTake = self.solve(idx - 1, nums, dp)

        dp[idx] = max(take, notTake)

        return dp[idx]

    def rob(self, nums: List[int]) -> int:
        dp = {}
        return self.solve(len(nums) - 1, nums, dp)


# Tabulation
# T.C. - O(n)
# S.C  - O(n)


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = {i: 0 for i in range(n)}
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            take, notTake = nums[i], 0

            if i - 2 >= 0:
                take += dp[i - 2]

            if i - 1 >= 0:
                notTake = dp[i - 1]

            dp[i] = max(take, notTake)

        return dp[n - 1]


# Space Optimized
# T.C. - O(n)
# S.C  - O(1)


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_prev = 0
        prev = nums[0]

        for i in range(1, len(nums)):
            take, notTake = nums[i], 0

            if i - 2 >= 0:
                take += prev_prev

            if i - 1 >= 0:
                notTake = prev

            prev_prev = prev
            prev = max(take, notTake)

        return prev
