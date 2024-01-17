# https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1 , Medium

# Recursion
# T.C. - O(n*wt*2^n)
# S.C  - O(n)


class Solution:
    def solve(self, W, wt, val, n):
        if W == 0 or n == 0:
            return 0

        take, notTake = 0, 0

        if wt[n] <= W:
            take = self.solve(W - wt[n], wt, val, n - 1) + val[n]
            notTake = self.solve(W, wt, val, n - 1)

        elif wt[n] > W:
            notTake = self.solve(W, wt, val, n - 1)

        return max(take, notTake)

    def knapSack(self, W, wt, val, n):
        return self.solve(W, wt, val, n - 1)


# Memoization
# T.C. - O(n*wt)
# S.C  - O(n)+O(n*wt)


class Solution:
    def solve(self, W, wt, val, n):
        if (n, W) in self.dp:
            return self.dp[(n, W)]
        if W == 0:
            return 0

        if n == 0:
            if wt[0] <= W:
                return val[0]
            else:
                return 0

        take, notTake = 0, 0

        if wt[n] <= W:
            take = self.solve(W - wt[n], wt, val, n - 1) + val[n]
            notTake = self.solve(W, wt, val, n - 1)

        elif wt[n] > W:
            notTake = self.solve(W, wt, val, n - 1)

        self.dp[(n, W)] = max(take, notTake)

        return self.dp[(n, W)]

    def knapSack(self, W, wt, val, n):
        self.dp = {}
        return self.solve(W, wt, val, n - 1)


# Tabulation
# T.C. - O(n*wt)
# S.C  - O(n*wt)


class Solution:
    def knapSack(self, W, wt, val, n):
        dp = [[-1 for _ in range(W + 1)] for _ in range(n)]

        for N in range(n):
            for w in range(W + 1):
                if w == 0:
                    dp[N][w] = 0
                elif N == 0:
                    if wt[0] <= w:
                        dp[N][w] = val[0]
                    else:
                        dp[N][w] = 0
                else:
                    take, notTake = 0, 0
                    if wt[N] <= w:
                        take = dp[N - 1][w - wt[N]] + val[N]
                        notTake = dp[N - 1][w]
                    elif wt[N] > w:
                        notTake = dp[N - 1][w]

                    dp[N][w] = max(take, notTake)

        return dp[n - 1][W]


# Space Optimized
# T.C. - O(n*wt)
# S.C  - O(W)


class Solution:
    def knapSack(self, W, wt, val, n):
        dp = [-1 for _ in range(W + 1)]

        for N in range(n):
            tmp = [-1 for _ in range(W + 1)]
            for w in range(W + 1):
                if w == 0:
                    tmp[w] = 0
                elif N == 0:
                    if wt[0] <= w:
                        tmp[w] = val[0]
                    else:
                        tmp[w] = 0
                else:
                    take, notTake = 0, 0
                    if wt[N] <= w:
                        take = dp[w - wt[N]] + val[N]
                        notTake = dp[w]
                    elif wt[N] > w:
                        notTake = dp[w]

                    tmp[w] = max(take, notTake)
            dp = tmp

        return dp[W]
