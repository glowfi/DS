#  https://leetcode.com/problems/ipo, Hard


# Optimal
# T.C. - O(NLogN+KLogN)
# S.C  - O(K)

# Intuition
# We have a starting capital w, at first we can only start
# projects less than equal to our w, we are going to be greedy
# and start project that gives us max profit
# we first scan the captial_profit_arr until our current capital w permits
# we keep pushing the profit to a max heap
# then we pop the project with max profit and start it
# We keep doing this k times


import heapq


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        captial_profit_arr = [(capital[i], profits[i]) for i in range(len(profits))]
        captial_profit_arr.sort(key=lambda x: x[0])

        i = 0
        max_heap = []

        for _ in range(k):
            while i < len(captial_profit_arr) and captial_profit_arr[i][0] <= w:
                heapq.heappush(max_heap, captial_profit_arr[i][-1] * -1)
                i += 1

            if not max_heap:
                break

            w += heapq.heappop(max_heap) * -1

        return w
