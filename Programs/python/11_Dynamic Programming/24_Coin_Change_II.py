# https://leetcode.com/problems/coin-change-ii/ , Medium

# Recursion
# T.C. - O(n*amt*2^n)
# S.C  - O(n)


class Solution:
    def solve(self, ind, cap, coins):
        if ind == 0:
            if cap % coins[ind] == 0:
                return 1
            return 0

        take = 0

        if coins[ind] <= cap:
            take = self.solve(ind, cap - coins[ind], coins)

        notTake = self.solve(ind - 1, cap, coins)

        return take + notTake

    def change(self, amount: int, coins: list[int]) -> int:
        if amount == 0:
            return 1
        data = self.solve(len(coins) - 1, amount, coins)
        return data


# Memoization
# T.C. - O(n*amt*n)
# S.C  - O(n*amt)+O(n)


class Solution:
    def solve(self, ind, cap, coins, dp):
        if (ind, cap) in dp:
            return dp[(ind, cap)]

        if ind == 0:
            if cap % coins[ind] == 0:
                return 1
            return 0

        take = 0

        if coins[ind] <= cap:
            take = self.solve(ind, cap - coins[ind], coins, dp)

        notTake = self.solve(ind - 1, cap, coins, dp)

        dp[(ind, cap)] = take + notTake

        return dp[(ind, cap)]

    def change(self, amount: int, coins: list[int]) -> int:
        dp = {}
        if amount == 0:
            return 1
        data = self.solve(len(coins) - 1, amount, coins, dp)
        return data


# Tabulation
# T.C. - O(n*amt)
# S.C  - O(n*amt)


class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        if amount == 0:
            return 1

        dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins))]

        for ind in range(len(coins)):
            for cap in range(amount + 1):
                if ind == 0:
                    if cap % coins[ind] == 0:
                        dp[ind][cap] = 1
                    else:
                        dp[ind][cap] = 0
                else:
                    take = 0
                    if coins[ind] <= cap:
                        take = dp[ind][cap - coins[ind]]
                    notTake = dp[ind - 1][cap]
                    dp[ind][cap] = take + notTake

        data = dp[len(coins) - 1][amount]
        return data


# Space Optimized
# T.C. - O(n*amt)
# S.C  - O(amt)


class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        if amount == 0:
            return 1

        dp = [0 for _ in range(amount + 1)]

        for ind in range(len(coins)):
            tmp = [0 for _ in range(amount + 1)]
            for cap in range(amount + 1):
                if ind == 0:
                    if cap % coins[ind] == 0:
                        tmp[cap] = 1
                    else:
                        tmp[cap] = 0
                else:
                    take = 0
                    if coins[ind] <= cap:
                        take = tmp[cap - coins[ind]]
                    notTake = dp[cap]
                    tmp[cap] = take + notTake
            dp = tmp

        data = dp[amount]
        return data
