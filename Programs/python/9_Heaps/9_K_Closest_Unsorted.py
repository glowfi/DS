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


# Optimal [max heap]
# T.C. - O(nlog(n))
# S.C  - O(1)

import heapq


class Solution:
    def Kclosest(self, arr, n, x, k):
        max_heap = []
        for num in arr:
            if len(max_heap) < k:
                heapq.heappush(max_heap, (-abs(num - x), num))
            else:
                if abs(num - x) < -max_heap[0][0]:
                    heapq.heappop(max_heap)
                    heapq.heappush(max_heap, (-abs(num - x), num))
        return sorted([num for _, num in max_heap])
