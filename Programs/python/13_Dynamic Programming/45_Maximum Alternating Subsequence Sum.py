# https://leetcode.com/problems/maximum-alternating-subsequence-sum/ , Medium

# Recursion
# T.C. - O(2^n)
# S.C  - O(n)


class Solution:
    def solve(self, idx, flag, nums):
        if idx == len(nums):
            return 0

        # Take
        take = (nums[idx] * flag) + self.solve(idx + 1, flag * -1, nums)

        # Not Take
        notTake = 0 + self.solve(idx + 1, flag, nums)

        return max(take, notTake)

    def maxAlternatingSum(self, nums: list[int]) -> int:
        return self.solve(0, 1, nums)


# Memoization
# T.C. - O(n)
# S.C  - O(n)+O(n*2)


class Solution:
    def solve(self, idx, flag, nums, dp):
        if (idx, flag) in dp:
            return dp[(idx, flag)]
        if idx == len(nums):
            return 0

        # Take
        take = (nums[idx] * flag) + self.solve(idx + 1, flag * -1, nums, dp)

        # Not Take
        notTake = 0 + self.solve(idx + 1, flag, nums, dp)

        dp[(idx, flag)] = max(take, notTake)

        return dp[(idx, flag)]

    def maxAlternatingSum(self, nums: list[int]) -> int:
        return self.solve(0, 1, nums, {})


# Tabulation
# T.C. - O(n)
# S.C  - O(n*2)


class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        dp = {}

        for i in range(len(nums) + 1):
            for j in range(-1, 2):
                if j == 0:
                    continue
                else:
                    dp[(i, j)] = 0

        for idx in range(len(nums), -1, -1):
            for flag in range(-1, 2):
                if flag == 0:
                    continue
                elif idx == len(nums):
                    dp[(idx, flag)] = 0
                else:
                    take = (nums[idx] * flag) + dp[(idx + 1, flag * -1)]
                    notTake = 0 + dp[(idx + 1, flag)]

                    dp[(idx, flag)] = max(take, notTake)

        return dp[(0, 1)]


# Space Optimized
# T.C. - O(n)
# S.C  - O(2)


class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        dp = {}
        curr = {}

        for j in range(-1, 2):
            if j == 0:
                continue
            else:
                dp[j] = 0
                curr[j] = 0

        for idx in range(len(nums), -1, -1):
            for flag in range(-1, 2):
                if flag == 0:
                    continue
                elif idx == len(nums):
                    curr[flag] = 0
                else:
                    take = (nums[idx] * flag) + dp[flag * -1]
                    notTake = 0 + dp[flag]

                    curr[flag] = max(take, notTake)

            dp = curr

        return dp[1]
