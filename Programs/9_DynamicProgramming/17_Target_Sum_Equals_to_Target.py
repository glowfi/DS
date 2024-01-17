# https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1 , Medium

# Recursion
# T.C. - O(2^n*n*sm)
# S.C  - O(n)


class Solution:
    def solve(self, arr, target, N):
        if target == 0:
            return True

        if N == 0:
            if arr[0] == target:
                return True
            return False

        take, notTake = False, False

        if arr[N] <= target:
            take = self.solve(arr, target - arr[N], N - 1)
            notTake = self.solve(arr, target, N - 1)

        elif arr[N] > target:
            notTake = self.solve(arr, target, N - 1)

        return take or notTake

    def isSubsetSum(self, N, arr, sum):
        return self.solve(arr, sum, N - 1)


# Memoization
# T.C. - O(n*sm)
# S.C  - O(n)+O(n*sm)


class Solution:
    def solve(self, arr, target, N):
        if (target, N) in self.dp:
            return self.dp[(target, N)]

        if target == 0:
            return True

        if N == 0:
            if arr[0] == target:
                return True
            return False

        take, notTake = False, False

        if arr[N] <= target:
            take = self.solve(arr, target - arr[N], N - 1)
            notTake = self.solve(arr, target, N - 1)

        elif arr[N] > target:
            notTake = self.solve(arr, target, N - 1)

        self.dp[(N, target)] = take or notTake

        return take or notTake

    def isSubsetSum(self, N, arr, sum):
        self.dp = {}
        return self.solve(arr, sum, N - 1)


# Tabulation
# T.C. - O(n)
# S.C  - O(n*sm)


class Solution:
    def isSubsetSum(self, N, arr, sum):
        dp = [[False for _ in range(sum + 1)] for _ in range(N)]

        for n in range(N):
            for target in range(sum + 1):
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

        return dp[N - 1][sum]


# Space Optimized
# T.C. - O(n)
# S.C  - O(sm)


class Solution:
    def isSubsetSum(self, N, arr, sum):
        dp = [False for _ in range(sum + 1)]

        for n in range(N):
            tmp = [False for _ in range(sum + 1)]
            for target in range(sum + 1):
                if target == 0:
                    tmp[target] = True

                elif n == 0:
                    if arr[0] == target:
                        tmp[target] = True
                    else:
                        tmp[target] = False
                else:
                    take, notTake = False, False
                    if arr[n] <= target:
                        take = dp[target - arr[n]]
                        notTake = dp[target]

                    elif arr[n] > target:
                        notTake = dp[target]

                    tmp[target] = take or notTake

            dp = tmp

        return dp[sum]
