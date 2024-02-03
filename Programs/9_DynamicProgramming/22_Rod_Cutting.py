# https://www.geeksforgeeks.org/problems/rod-cutting0840/1 , Medium

# Recursion
# T.C. - O(n*price*2^n)
# S.C  - O(n)


class Solution:
    def solve(self, ind, cap, length, price):
        if ind == 0:
            if length[ind] <= cap:
                return (cap // length[ind]) * price[ind]
            return 0

        take = 0
        if length[ind] <= cap:
            take = price[ind] + self.solve(ind, cap - length[ind], length, price)
        notTake = self.solve(ind - 1, cap, length, price)

        return max(take, notTake)

    def cutRod(self, price, n):
        length = [i for i in range(1, n + 1)]
        return self.solve(n - 1, n, length, price)


# Memoization
# T.C. - O(n*price*n)
# S.C  - O(n)+O(n)


class Solution:
    def solve(self, ind, cap, length, price, dp):
        if (ind, cap) in dp:
            return dp[(ind, cap)]
        if ind == 0:
            if length[ind] <= cap:
                return (cap // length[ind]) * price[ind]
            return 0

        take = 0
        if length[ind] <= cap:
            take = price[ind] + self.solve(ind, cap - length[ind], length, price, dp)
        notTake = self.solve(ind - 1, cap, length, price, dp)

        dp[(ind, cap)] = max(take, notTake)

        return dp[(ind, cap)]

    def cutRod(self, price, n):
        length = [i for i in range(1, n + 1)]
        dp = {}
        return self.solve(n - 1, n, length, price, dp)


# Tabulation
# T.C. - O(n*n)
# S.C  - O(n*n)


class Solution:
    def cutRod(self, price, n):
        length = [i for i in range(1, n + 1)]
        dp = [[0 for _ in range(n + 1)] for _ in range(n)]

        for ind in range(n):
            for cap in range(n + 1):
                if ind == 0:
                    if length[ind] <= cap:
                        dp[ind][cap] = (cap // length[ind]) * price[ind]
                    else:
                        dp[ind][cap] = 0
                else:
                    take = 0
                    if length[ind] <= cap:
                        take = price[ind] + dp[ind][cap - length[ind]]
                    notTake = dp[ind - 1][cap]
                    dp[ind][cap] = max(take, notTake)

        return dp[n - 1][n]


# Space Optimized
# T.C. - O(n*n)
# S.C  - O(n)


class Solution:
    def cutRod(self, price, n):
        length = [i for i in range(1, n + 1)]
        dp = [0 for _ in range(n + 1)]

        for ind in range(n):
            tmp = [0 for _ in range(n + 1)]
            for cap in range(n + 1):
                if ind == 0:
                    if length[ind] <= cap:
                        tmp[cap] = (cap // length[ind]) * price[ind]
                    else:
                        tmp[cap] = 0
                else:
                    take = 0
                    if length[ind] <= cap:
                        take = price[ind] + tmp[cap - length[ind]]
                    notTake = dp[cap]
                    tmp[cap] = max(take, notTake)
            dp = tmp

        return dp[n]
