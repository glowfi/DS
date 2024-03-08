# https://www.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1 , Hard

# Rules
# 1. Find i and j
# 2. Find Base Condition
# 3. Find valid loop scheme for k
# 4. Use the temp funciton calls


# Recursion
# T.C. - O(2**n)
# S.C  - O(N)


class Solution:
    def solve(self, i, j, arr):
        if i >= j:
            return 0

        mn = float("inf")

        for k in range(i, j):
            curr = (
                self.solve(i, k, arr)
                + self.solve(k + 1, j, arr)
                + (arr[i - 1] * arr[k] * arr[j])
            )
            mn = min(curr, mn)

        return mn

    def matrixMultiplication(self, N, arr):
        return self.solve(1, len(arr) - 1, arr)


# Memoization
# T.C. - O(N*N*N)
# S.C  - O(N*N)+O(N)


class Solution:
    def solve(self, i, j, arr, dp):
        if (i, j) in dp:
            return dp[(i, j)]

        if i >= j:
            return 0

        mn = float("inf")

        for k in range(i, j):
            curr = (
                self.solve(i, k, arr, dp)
                + self.solve(k + 1, j, arr, dp)
                + (arr[i - 1] * arr[k] * arr[j])
            )
            mn = min(curr, mn)

        dp[(i, j)] = mn

        return dp[(i, j)]

    def matrixMultiplication(self, N, arr):
        return self.solve(1, len(arr) - 1, arr, {})


# Tabulation
# T.C. - O(N^3)
# S.C  - O(N^2)


class Solution:
    def matrixMultiplication(self, N, arr):
        dp = [[0 for _ in range(len(arr))] for _ in range(len(arr))]

        for i in range(len(arr) - 1, 0, -1):
            for j in range(i + 1, len(arr)):
                mn = float("inf")
                for k in range(i, j):
                    curr = dp[i][k] + dp[k + 1][j] + (arr[i - 1] * arr[k] * arr[j])
                    if curr < mn:
                        mn = curr
                if mn != float("inf"):
                    dp[i][j] = mn

        return dp[1][len(arr) - 1]
