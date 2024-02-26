# https://leetcode.com/problems/longest-increasing-subsequence/ , Medium

# Recursion
# T.C. - O(2^n)
# S.C  - O(n)


class Solution:
    def solve(self, currIdx, prevIdx, nums):
        if currIdx == len(nums):
            return 0

        take = 0

        if prevIdx == -1 or nums[currIdx] > nums[prevIdx]:
            take = 1 + self.solve(currIdx + 1, currIdx, nums)
        notTake = 0 + self.solve(currIdx + 1, prevIdx, nums)

        return max(take, notTake)

    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.solve(0, -1, nums)


# Memoization
# T.C. - O(n)
# S.C  - O(n)+O(n^2)


class Solution:
    def solve(self, currIdx, prevIdx, nums, dp):
        if currIdx == len(nums):
            return 0

        if dp[currIdx][prevIdx + 1] != -1:
            return dp[currIdx][prevIdx + 1]

        take = 0

        if prevIdx == -1 or nums[currIdx] > nums[prevIdx]:
            take = 1 + self.solve(currIdx + 1, currIdx, nums, dp)
        notTake = 0 + self.solve(currIdx + 1, prevIdx, nums, dp)

        dp[currIdx][prevIdx + 1] = max(take, notTake)

        return dp[currIdx][prevIdx + 1]

    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [[-1 for _ in range(len(nums) + 1)] for _ in range(len(nums) + 1)]
        return self.solve(0, -1, nums, dp)


# Tabulation
# T.C. - O(n^2)
# S.C  - O(n^2)


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [[0 for _ in range(len(nums) + 1)] for _ in range(len(nums) + 1)]

        for currIdx in range(len(nums), -1, -1):
            for prevIdx in range(currIdx - 1, -2, -1):
                if currIdx == len(nums):
                    dp[currIdx][prevIdx + 1] = 0
                else:
                    take = 0

                    if prevIdx == -1 or nums[currIdx] > nums[prevIdx]:
                        take = 1 + dp[currIdx + 1][currIdx + 1]
                    notTake = 0 + dp[currIdx + 1][prevIdx + 1]

                    dp[currIdx][prevIdx + 1] = max(take, notTake)

        return dp[0][-1 + 1]


# Space Optimized
# T.C. - O(n^2)
# S.C  - O(n)


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums) + 1)]
        tmp = [0 for _ in range(len(nums) + 1)]

        for currIdx in range(len(nums), -1, -1):
            for prevIdx in range(currIdx - 1, -2, -1):
                if currIdx == len(nums):
                    tmp[prevIdx + 1] = 0
                else:
                    take = 0

                    if prevIdx == -1 or nums[currIdx] > nums[prevIdx]:
                        take = 1 + dp[currIdx + 1]
                    notTake = 0 + dp[prevIdx + 1]

                    tmp[prevIdx + 1] = max(take, notTake)
            dp = tmp

        return dp[-1 + 1]


# Optimal (V1)
# T.C  - O(n^2)
# S.C. - O(n)

# Note :Keep checking whether previous elemnts can become part of the longest-increasing-subsequence


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        ans = 1

        for idx in range(len(nums)):
            for prevIdx in range(idx):
                if nums[prevIdx] < nums[idx]:
                    dp[idx] = max(dp[idx], 1 + dp[prevIdx])
                    ans = max(dp[idx], ans)

        return ans


# Optimal (V2)
# T.C  - O(nlog(n))
# S.C. - O(n)


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        pass
