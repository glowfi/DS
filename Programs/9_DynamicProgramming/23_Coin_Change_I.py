# https://leetcode.com/problems/coin-change/description/ , Medium

# Recursion
# T.C. - O(n*amount*2^n)
# S.C  - O(n)


class Solution:
    def solve(self, ind, cap, coins):
        if ind == 0:
            if cap % coins[ind] == 0:
                return cap // coins[ind]
            return float("inf")

        take = float("inf")

        if coins[ind] <= cap:
            take = 1 + self.solve(ind, cap - coins[ind], coins)

        notTake = 0 + self.solve(ind - 1, cap, coins)

        return min(take, notTake)

    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount == 0:
            return 0

        data = self.solve(len(coins) - 1, amount, coins)
        if data == float("inf"):
            return -1
        return data


# Memoization
# T.C. - O(n*amt)
# S.C  - O(n*amt)+O(n)


class Solution:
    def solve(self, ind, cap, coins, dp):
        if (ind, cap) in dp:
            return dp[(ind, cap)]

        if ind == 0:
            if cap % coins[ind] == 0:
                return cap // coins[ind]
            return float("inf")

        take = float("inf")

        if coins[ind] <= cap:
            take = 1 + self.solve(ind, cap - coins[ind], coins, dp)

        notTake = 0 + self.solve(ind - 1, cap, coins, dp)

        dp[(ind, cap)] = min(take, notTake)

        return dp[(ind, cap)]

    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = {}
        if amount == 0:
            return 0

        data = self.solve(len(coins) - 1, amount, coins, dp)
        if data == float("inf"):
            return -1
        return data


# Tabulation
# T.C. - O(n*amt)
# S.C  - O(n*amt)


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins))]

        for ind in range(len(coins)):
            for cap in range(amount + 1):
                if ind == 0:
                    if cap % coins[ind] == 0:
                        dp[ind][cap] = cap // coins[ind]
                    else:
                        dp[ind][cap] = float("inf")
                else:
                    take = float("inf")
                    if coins[ind] <= cap:
                        take = 1 + dp[ind][cap - coins[ind]]
                    notTake = 0 + dp[ind - 1][cap]

                    dp[ind][cap] = min(take, notTake)

        data = dp[len(coins) - 1][amount]
        if data == float("inf"):
            return -1
        return data


# Space Optimized
# T.C. - O(n*amt)
# S.C  - O(amt)


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = [0 for _ in range(amount + 1)]

        for ind in range(len(coins)):
            tmp = [0 for _ in range(amount + 1)]
            for cap in range(amount + 1):
                if ind == 0:
                    if cap % coins[ind] == 0:
                        tmp[cap] = cap // coins[ind]
                    else:
                        tmp[cap] = float("inf")
                else:
                    take = float("inf")
                    if coins[ind] <= cap:
                        take = 1 + tmp[cap - coins[ind]]
                    notTake = 0 + dp[cap]

                    tmp[cap] = min(take, notTake)
            dp = tmp

        data = dp[amount]
        if data == float("inf"):
            return -1
        return data
