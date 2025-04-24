# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/ , Hard

# Recursion
# T.C. - O(2^n)
# S.C  - O(n)


class Solution:
    def solve(self, idx, canBuy, k, prices):
        # Base Case
        if k == 0:
            return 0

        if idx == len(prices):
            return 0

        # All ways
        profit = 0

        if canBuy:
            buy = -prices[idx] + self.solve(idx + 1, 0, k, prices)
            notBuy = 0 + self.solve(idx + 1, 1, k, prices)
            profit = max(buy, notBuy)
        else:
            sell = prices[idx] + self.solve(idx + 1, 1, k - 1, prices)
            notSell = 0 + self.solve(idx + 1, 0, k, prices)
            profit = max(sell, notSell)

        return profit

    def maxProfit(self, prices: list[int]) -> int:
        return self.solve(0, 1, 2, prices)


# Memoization
# T.C. - O(n)
# S.C  - O(n)+O(n^2)


class Solution:
    def solve(self, idx, canBuy, k, prices, dp):
        # Base Case
        if (idx, canBuy, k) in dp:
            return dp[(idx, canBuy, k)]

        if k == 0:
            return 0

        if idx == len(prices):
            return 0

        # All ways
        profit = 0

        if canBuy:
            buy = -prices[idx] + self.solve(idx + 1, 0, k, prices, dp)
            notBuy = 0 + self.solve(idx + 1, 1, k, prices, dp)
            profit = max(buy, notBuy)
        else:
            sell = prices[idx] + self.solve(idx + 1, 1, k - 1, prices, dp)
            notSell = 0 + self.solve(idx + 1, 0, k, prices, dp)
            profit = max(sell, notSell)

        dp[(idx, canBuy, k)] = profit

        return dp[(idx, canBuy, k)]

    def maxProfit(self, prices: list[int]) -> int:
        return self.solve(0, 1, 2, prices, {})


# Tabulation
# T.C. - O(n*2*2)
# S.C  - O(n*2*2)


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        k = 2
        dp = [
            [[num for num in range(k + 1)] for _ in range(0, 2)]
            for _ in range(len(prices) + 1)
        ]

        for idx in range(len(prices), -1, -1):
            for canBuy in range(0, 2):
                for k in range(k + 1):
                    if k == 0:
                        dp[idx][canBuy][k] = 0
                    elif idx == len(prices):
                        dp[idx][canBuy][k] = 0
                    else:
                        profit = 0
                        if canBuy:
                            buy = -prices[idx] + dp[idx + 1][0][k]
                            notBuy = 0 + dp[idx + 1][1][k]
                            profit = max(buy, notBuy)
                        else:
                            sell = prices[idx] + dp[idx + 1][1][k - 1]
                            notSell = 0 + dp[idx + 1][0][k]
                            profit = max(sell, notSell)
                        dp[idx][canBuy][k] = profit

        return dp[0][1][2]


# Space Optimized
# T.C. - O(n*2*2)
# S.C  - O(k*2)+O(k*2)


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        k = 2
        dp = [[num for num in range(k + 1)] for _ in range(0, 2)]
        tmp = [[num for num in range(k + 1)] for _ in range(0, 2)]

        for idx in range(len(prices), -1, -1):
            for canBuy in range(0, 2):
                for k in range(k + 1):
                    if k == 0:
                        tmp[canBuy][k] = 0
                    elif idx == len(prices):
                        tmp[canBuy][k] = 0
                    else:
                        profit = 0
                        if canBuy:
                            buy = -prices[idx] + dp[0][k]
                            notBuy = 0 + dp[1][k]
                            profit = max(buy, notBuy)
                        else:
                            sell = prices[idx] + dp[1][k - 1]
                            notSell = 0 + dp[0][k]
                            profit = max(sell, notSell)
                        tmp[canBuy][k] = profit
                dp = tmp

        return dp[1][2]
