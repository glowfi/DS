# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/,Easy

# Optimal
# T.C. -> O(n)
# S.C. -> O(1)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minSoFar = prices[0]

        for i in range(1, len(prices)):
            currProfit = prices[i] - minSoFar
            if prices[i] < minSoFar:
                minSoFar = prices[i]
            profit = max(currProfit, profit)
        return profit
