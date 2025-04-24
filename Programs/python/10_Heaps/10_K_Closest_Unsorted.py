# https://www.geeksforgeeks.org/problems/lucys-neighbours--141631/1 , Medium


# Optimal [min heap]
# T.C. - O(nlog(n))
# S.C  - O(1)

import heapq


class Solution:
    def Kclosest(self, arr, n, x, k):
        heap = []

        for i in arr:
            heapq.heappush(heap, [abs(i - x), i])

        res = []
        while k:
            res.append(heapq.heappop(heap)[-1])
            k -= 1

        return sorted(res)
