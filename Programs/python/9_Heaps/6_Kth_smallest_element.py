# https://www.geeksforgeeks.org/problems/kth-smallest-element5635/1 , Medium


# Better
# T.C. - O(nlog(n))
# S.C  - O(1)


class Solution:

    def kthSmallest(self, arr, k):
        return sorted(arr)[k - 1]


# Optimal
# T.C. - O(nlog(k))
# S.C  - O(log(n))

import heapq


class Solution:

    def kthSmallest(self, arr, k):
        heap = []

        for i in range(len(arr)):
            elem = arr[i]
            heapq.heappush(heap, elem * -1)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0] * -1


# Optimal [order maintained]
# T.C. - O(nlog(k))
# S.C  - O(log(n))

import heapq


class Solution:

    def kthSmallest(self, arr, k):
        heap = []
        for num in arr:
            if len(heap) < k:
                heapq.heappush(heap, num * -1)
            else:
                if num < heap[0] * -1:
                    heapq.heappop(heap)
                    heapq.heappush(heap, num * -1)

        return heap[0] * -1
