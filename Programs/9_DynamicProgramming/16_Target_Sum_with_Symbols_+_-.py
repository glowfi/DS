# https://leetcode.com/problems/target-sum/ , Medium


# Recursion
# T.C. - O(2^n)
# S.C  - O(n)


class Solution:
    def solve(self, idx, sm, nums, target):
        if idx == len(nums):
            if sm == target:
                return 1
            return 0

        l = self.solve(idx + 1, sm + nums[idx] * 1, nums, target)
        r = self.solve(idx + 1, sm + (nums[idx] * -1), nums, target)

        return l + r

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.solve(0, 0, nums, target)


# Memoization
# T.C. - O(n)
# S.C  - O(n)+O(n)


class Solution:
    def solve(self, idx, sm, nums, target, dp):
        if (idx, sm) in dp:
            return dp[(idx, sm)]

        if idx == len(nums):
            if sm == target:
                return 1
            return 0

        l = self.solve(idx + 1, sm + nums[idx] * 1, nums, target, dp)
        r = self.solve(idx + 1, sm + (nums[idx] * -1), nums, target, dp)

        dp[(idx, sm)] = l + r

        return dp[(idx, sm)]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        return self.solve(0, 0, nums, target, dp)


# Tabulation
# T.C. - O(n)
# S.C  - O(n)

# Space Optimized
# T.C. -
# S.C  -
