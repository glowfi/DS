# https://www.geeksforgeeks.org/problems/knapsack-with-duplicate-items4201/1 , Medium

# Recursion
# T.C. - O(n*wt*2^n)
# S.C  - O(n)


class Solution:
    def solve(self, ind, cap, val, wt):
        if ind == 0:
            if wt[0] <= cap:
                return val[0] * (cap // wt[0])
            return 0

        take = 0

        if wt[ind] <= cap:
            take = val[ind] + self.solve(ind, cap - wt[ind], val, wt)

        notTake = self.solve(ind - 1, cap, val, wt)

        return max(take, notTake)

    def knapSack(self, N, W, val, wt):
        return self.solve(N - 1, W, val, wt)


# Memoization
# T.C. - O(n*wt*2^n)
# S.C  - O(n)+O(n)


class Solution:
    def solve(self, ind, cap, val, wt, dp):
        if (ind, cap) in dp:
            return dp[(ind, cap)]

        if ind == 0:
            if wt[0] <= cap:
                return val[0] * (cap // wt[0])
            return 0

        take = 0

        if wt[ind] <= cap:
            take = val[ind] + self.solve(ind, cap - wt[ind], val, wt, dp)

        notTake = self.solve(ind - 1, cap, val, wt, dp)

        dp[(ind, cap)] = max(take, notTake)

        return max(take, notTake)

    def knapSack(self, N, W, val, wt):
        dp = {}
        return self.solve(N - 1, W, val, wt, dp)


# Tabulation
# T.C. - O(n*wt)
# S.C  - O(n^2)


class Solution:
    def knapSack(self, N, W, val, wt):
        dp = [[0 for _ in range(W + 1)] for _ in range(N)]

        for ind in range(N):
            for cap in range(W + 1):
                if ind == 0:
                    if wt[0] <= cap:
                        dp[ind][cap] = val[0] * (cap // wt[0])
                    else:
                        dp[ind][cap] = 0
                else:
                    take = 0
                    if wt[ind] <= cap:
                        take = val[ind] + dp[ind][cap - wt[ind]]
                    notTake = 0 + dp[ind - 1][cap]
                    dp[ind][cap] = max(take, notTake)

        return dp[N - 1][W]


# Space Optimized
# T.C. - O(n*wt)
# S.C  - O(cap)


class Solution:
    def knapSack(self, N, W, val, wt):
        dp = [0 for _ in range(W + 1)]

        for ind in range(N):
            tmp = [0 for _ in range(W + 1)]
            for cap in range(W + 1):
                if ind == 0:
                    if wt[0] <= cap:
                        tmp[cap] = val[0] * (cap // wt[0])
                    else:
                        tmp[cap] = 0
                else:
                    take = 0
                    if wt[ind] <= cap:
                        take = val[ind] + tmp[cap - wt[ind]]
                    notTake = 0 + dp[cap]
                    tmp[cap] = max(take, notTake)
            dp = tmp

        return dp[W]
