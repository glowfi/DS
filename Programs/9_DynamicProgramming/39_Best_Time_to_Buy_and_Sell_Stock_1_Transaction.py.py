# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/ , Easy


# Optimal
# T.C. - O(n)
# S.C  - O(1)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        mxProfit = 0

        while r < len(prices):
            # isProfitable
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                mxProfit = max(mxProfit, profit)
            else:
                l = r
            r += 1

        return mxProfit


# Space Optimized
# T.C. - O(n*2*k)
# S.C  - O(k*2)+O(k*2)
# k=1


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        k = 1
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

        return dp[1][k]
