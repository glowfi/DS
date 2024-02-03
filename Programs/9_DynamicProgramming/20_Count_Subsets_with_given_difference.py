# https://www.geeksforgeeks.org/problems/partitions-with-given-difference/1 , Medium

# Recursion
# T.C. - O(n*sm*2^n)
# S.C  - O(n)


class Solution:
    def solve(self, idx, sm, arr):
        if idx == 0:
            if sm == 0 and arr[0] == 0:
                return 2
            if sm == arr[0] or sm == 0:
                return 1
            return 0

        take = 0
        MOD = (10**9) + 7
        if arr[idx] <= sm:
            take = self.solve(idx - 1, sm - arr[idx], arr)
        notTake = self.solve(idx - 1, sm, arr)

        return (take + notTake) % MOD

    def countPartitions(self, n, d, arr):
        sm = d + sum(arr)
        if sm % 2 == 1:
            return 0

        return self.solve(n - 1, sm // 2, arr)


# Memoization
# T.C. - O(n*sm*n)
# S.C  - O(n)+O(n*sm)


class Solution:
    def solve(self, idx, sm, arr, dp):
        if (idx, sm) in dp:
            return dp[(idx, sm)]

        if idx == 0:
            if sm == 0 and arr[0] == 0:
                return 2
            if sm == arr[0] or sm == 0:
                return 1
            return 0

        take = 0
        MOD = (10**9) + 7
        if arr[idx] <= sm:
            take = self.solve(idx - 1, sm - arr[idx], arr, dp)
        notTake = self.solve(idx - 1, sm, arr, dp)

        dp[(idx, sm)] = (take + notTake) % MOD

        return dp[(idx, sm)]

    def countPartitions(self, n, d, arr):
        dp = {}
        sm = d + sum(arr)
        if sm % 2 == 1:
            return 0

        return self.solve(n - 1, sm // 2, arr, dp)


# Tabulation
# T.C. - O(n*sm)
# S.C  - O(n*sm)


class Solution:
    def countPartitions(self, n, d, arr):
        _sm = d + sum(arr)
        if _sm % 2 == 1:
            return 0

        dp = [[0 for _ in range((_sm // 2) + 1)] for _ in range(n)]
        MOD = (10**9) + 7

        for idx in range(n):
            for sm in range((_sm // 2) + 1):
                if idx == 0:
                    if sm == 0 and arr[0] == 0:
                        dp[idx][sm] = 2
                    elif sm == arr[0] or sm == 0:
                        dp[idx][sm] = 1
                    else:
                        dp[idx][sm] = 0
                else:
                    take = 0
                    if arr[idx] <= sm:
                        take = dp[idx - 1][sm - arr[idx]]
                    notTake = dp[idx - 1][sm]

                    dp[idx][sm] = (take + notTake) % MOD

        return dp[n - 1][_sm // 2]


# Space Optimized
# T.C. - O(n*sm)
# S.C  - O(sm)


class Solution:
    def countPartitions(self, n, d, arr):
        _sm = d + sum(arr)
        if _sm % 2 == 1:
            return 0

        dp = [0 for _ in range((_sm // 2) + 1)]
        MOD = (10**9) + 7

        for idx in range(n):
            tmp = [0 for _ in range((_sm // 2) + 1)]
            for sm in range((_sm // 2) + 1):
                if idx == 0:
                    if sm == 0 and arr[0] == 0:
                        tmp[sm] = 2
                    elif sm == arr[0] or sm == 0:
                        tmp[sm] = 1
                    else:
                        tmp[sm] = 0
                else:
                    take = 0
                    if arr[idx] <= sm:
                        take = dp[sm - arr[idx]]
                    notTake = dp[sm]

                    tmp[sm] = (take + notTake) % MOD
            dp = tmp

        return dp[_sm // 2]
