# https://leetcode.com/problems/best-time-to-buy-and-sell-stock, Easy, MaintainMinMaxSoFar

# Question
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.


# Constraints:

# 1 <= prices.length <= 10^5
# 0 <= prices[i] <= 10^4


# Optimal
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# Suppose you are at index i just ask yourself
# can i sell this stock on this day if i have
# the minimum stock cost from left side of the index
# buy in less price and sell in high price


from typing import List
import sys


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_cp_till_now = prices[0]
        max_profit = -sys.maxsize

        for i in range(len(prices)):
            max_profit = max(max_profit, prices[i] - min_cp_till_now)
            min_cp_till_now = min(min_cp_till_now, prices[i])

        return max_profit
