# https://leetcode.com/problems/partition-array-for-maximum-sum/ , Medium

# Recursion
# T.C. - O(2^n)
# S.C  - O(n)


class Solution:
    def solve(self, i, k, arr):
        if i == len(arr):
            return 0

        mx = float("-inf")
        mx_till_now = float("-inf")
        c = 0

        for j in range(i, min(len(arr), i + k)):
            c += 1
            mx_till_now = max(mx_till_now, arr[j])

            sm = c * mx_till_now + self.solve(j + 1, k, arr)
            if sm > mx:
                mx = sm

        return mx

    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        return self.solve(0, k, arr)


# Memoization
# T.C. - O(n^2)
# S.C  - O(n)+O(n)


class Solution:
    def solve(self, i, k, arr, dp):
        if i == len(arr):
            return 0

        if i in dp:
            return dp[i]

        mx = float("-inf")
        mx_till_now = float("-inf")
        c = 0

        for j in range(i, min(len(arr), i + k)):
            c += 1
            mx_till_now = max(mx_till_now, arr[j])

            sm = c * mx_till_now + self.solve(j + 1, k, arr, dp)
            if sm > mx:
                mx = sm

        dp[i] = mx

        return dp[i]

    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        return self.solve(0, k, arr, {})


# Tabulation
# T.C. - O(n^2)
# S.C  - O(n)


class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        dp = [0 for _ in range(len(arr) + 1)]

        for i in range(len(arr), -1, -1):
            if i == len(arr):
                dp[i] = 0
            else:
                mx = float("-inf")
                mx_till_now = float("-inf")
                c = 0
                for j in range(i, min(len(arr), i + k)):
                    c += 1
                    mx_till_now = max(mx_till_now, arr[j])

                    sm = c * mx_till_now + dp[j + 1]
                    if sm > mx:
                        mx = sm

                dp[i] = mx

        return dp[0]
