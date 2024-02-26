# https://www.geeksforgeeks.org/problems/longest-bitonic-subsequence0824/1 , Medium

# Optimal
# T.C. - O(n^2)+O(n^2)+O(n)
# S.C  - O(n)+O(n)


class Solution:
    def lengthOfLIS(self, nums):
        dp = [1 for _ in range(len(nums))]

        for idx in range(len(nums)):
            for prevIdx in range(idx):
                if nums[prevIdx] < nums[idx]:
                    dp[idx] = max(dp[idx], 1 + dp[prevIdx])

        dp1 = [1 for _ in range(len(nums))]
        for idx in range(len(nums) - 1, -1, -1):
            for prevIdx in range(len(nums) - 1, idx, -1):
                if nums[prevIdx] < nums[idx]:
                    dp1[idx] = max(dp1[idx], 1 + dp1[prevIdx])

        maxi = 0

        for i in range(len(dp)):
            maxi = max((dp[i] + dp1[i]) - 1, maxi)

        return maxi

    def LongestBitonicSequence(self, nums):
        return self.lengthOfLIS(nums)
