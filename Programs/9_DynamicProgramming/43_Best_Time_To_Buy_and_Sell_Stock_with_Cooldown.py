# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/ , Mediun

# Recursion
# T.C. - O(2^n)
# S.C  - O(n)


class Solution:
    def solve(self, idx, canBuy, prices):
        # Base Case
        if idx >= len(prices):
            return 0

        profit = 0

        # All Ways
        if canBuy:
            buy = -prices[idx] + self.solve(idx + 1, 0, prices)
            notBuy = self.solve(idx + 1, 1, prices)
            profit = max(buy, notBuy)
        else:
            sell = self.solve(idx + 2, 1, prices) + prices[idx]
            notSell = self.solve(idx + 1, 0, prices)
            profit = max(sell, notSell)

        return profit

    def maxProfit(self, prices: list[int]) -> int:
        return self.solve(0, 1, prices)


# Memoization
# T.C. - O(n)
# S.C  - O(n)+O(n^2)


class Solution:
    def solve(self, idx, canBuy, prices, dp):
        # Base Case
        if (idx, canBuy) in dp:
            return dp[(idx, canBuy)]

        if idx >= len(prices):
            return 0

        profit = 0

        # All Ways
        if canBuy:
            buy = -prices[idx] + self.solve(idx + 1, 0, prices, dp)
            notBuy = self.solve(idx + 1, 1, prices, dp)
            profit = max(buy, notBuy)
        else:
            sell = self.solve(idx + 2, 1, prices, dp) + prices[idx]
            notSell = self.solve(idx + 1, 0, prices, dp)
            profit = max(sell, notSell)

        dp[(idx, canBuy)] = profit

        return dp[(idx, canBuy)]

    def maxProfit(self, prices: list[int]) -> int:
        return self.solve(0, 1, prices, {})


# Tabulation
# T.C. - O(n*2)
# S.C  - O(n^2)


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        dp = [[j for j in range(2)] for _ in range(len(prices) + 1)]

        for idx in range(len(prices), -1, -1):
            for canBuy in range(2):
                if idx == len(prices):
                    dp[idx][canBuy] = 0
                else:
                    profit = 0
                    if canBuy:
                        buy = -prices[idx] + dp[idx + 1][0]
                        notBuy = dp[idx + 1][1]
                        profit = max(buy, notBuy)
                    else:
                        sell = (
                            0 if idx + 2 >= len(prices) else (dp[idx + 2][1])
                        ) + prices[idx]
                        notSell = dp[idx + 1][0]
                        profit = max(sell, notSell)

                    dp[idx][canBuy] = profit

        return dp[0][1]
