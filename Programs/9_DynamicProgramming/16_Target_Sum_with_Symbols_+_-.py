# https://leetcode.com/problems/target-sum/ , Medium


# Recursion
# T.C. - O(2^n)
# S.C  - O(n)


class Solution:
    def solve(self, idx, sm, nums):
        if idx == 0:
            c = 0
            if sm + (nums[idx] * 1) == 0:
                c += 1
            if sm + (nums[idx] * -1) == 0:
                c += 1
            return c

        l = self.solve(idx - 1, sm + nums[idx] * 1, nums)
        r = self.solve(idx - 1, sm + (nums[idx] * -1), nums)

        return l + r

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.solve(len(nums) - 1, target, nums)


# Memoization
# T.C. - O(n)
# S.C  - O(n)+O(n)


class Solution:
    def solve(self, idx, sm, nums, dp):
        if (idx, sm) in dp:
            return dp[(idx, sm)]

        if idx == 0:
            c = 0
            if sm + (nums[idx] * 1) == 0:
                c += 1
            if sm + (nums[idx] * -1) == 0:
                c += 1
            return c

        l = self.solve(idx - 1, sm + nums[idx] * 1, nums, dp)
        r = self.solve(idx - 1, sm + (nums[idx] * -1), nums, dp)

        dp[(idx, sm)] = l + r

        return dp[(idx, sm)]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        return self.solve(len(nums) - 1, target, nums, dp)


# Tabulation
# T.C. - O(n)
# S.C  - O(n)

# Space Optimized
# T.C. -
# S.C  -
