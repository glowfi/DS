# https://www.geeksforgeeks.org/problems/minimum-sum-partition3317/1 , Hard


# Tabulation
# T.C. - O(n*target)+O(n)+O(target)
# S.C  - O(n*target)


class Solution:
    def minDifference(self, arr, n):
        # code here
        sm = sum(arr)
        N = len(arr)
        dp = [[False for _ in range(sm + 1)] for _ in range(N)]

        for n in range(N):
            for target in range(sm + 1):
                if target == 0:
                    dp[n][target] = True

                elif n == 0:
                    if arr[0] == target:
                        dp[n][target] = True
                    else:
                        dp[n][target] = False
                else:
                    take, notTake = False, False
                    if arr[n] <= target:
                        take = dp[n - 1][target - arr[n]]
                        notTake = dp[n - 1][target]

                    elif arr[n] > target:
                        notTake = dp[n - 1][target]

                    dp[n][target] = take or notTake

        diff = float("inf")

        for target in range(sm + 1):
            if dp[N - 1][target] is True:
                diff = min(diff, abs((2 * target) - sm))

        return diff
