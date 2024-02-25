# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/ , Medium

# Space Optimized
# T.C. - O(n*2)
# S.C  - O(2)


class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        dp = [j for j in range(2)]

        for idx in range(len(prices), -1, -1):
            tmp = [j for j in range(2)]
            for canBuy in range(1, -1, -1):
                if idx == len(prices):
                    tmp[canBuy] = 0
                else:
                    profit = 0
                    if canBuy:
                        buy = -prices[idx] + dp[0]
                        notBuy = dp[1]
                        profit = max(buy, notBuy)
                    else:
                        sell = dp[1] + prices[idx] - fee
                        notSell = dp[0]
                        profit = max(sell, notSell)

                    tmp[canBuy] = profit
            dp = tmp

        return dp[1]
