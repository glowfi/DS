# https://www.geeksforgeeks.org/problems/minimum-cost-of-ropes-1587115620/1 , Medium


# Optimal
# T.C. - O(n) +O(n)
# S.C  - O(1)

# At any point choose 2 ropes with min value

import heapq


class Solution:
    def minCost(self, arr):
        if len(arr) == 0:
            return 0

        cost = 0

        heapq.heapify(arr)

        while len(arr) > 1:
            first, second = heapq.heappop(arr), heapq.heappop(arr)
            cost += first + second
            heapq.heappush(arr, first + second)

        return cost
