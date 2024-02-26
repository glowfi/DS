# https://leetcode.com/problems/largest-divisible-subset/ , Medium

# Optimal
# T.C. - O(n^2)
# S.C  - O(n)+O(n)


class Solution:
    def longestIncreasingSubsequence(self, N, arr):
        dp = [1 for _ in range(len(arr))]
        path_map = {idx: idx for idx in range(len(arr))}

        mx_le = 1
        mx_dp_idx = 0
        ans = []

        for idx in range(len(arr)):
            for prevIdx in range(idx):
                if arr[idx] % arr[prevIdx] == 0:
                    if 1 + dp[prevIdx] > dp[idx]:
                        dp[idx] = max(dp[idx], 1 + dp[prevIdx])
                        path_map[idx] = prevIdx
                        if dp[idx] > mx_le:
                            mx_le = dp[idx]
                            mx_dp_idx = idx

        start = mx_dp_idx

        while True:
            if path_map[start] == start:
                ans.append(arr[start])
                break
            ans.append(arr[start])
            start = path_map[start]

        return ans[::-1]

    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        return self.longestIncreasingSubsequence(len(nums), nums)
