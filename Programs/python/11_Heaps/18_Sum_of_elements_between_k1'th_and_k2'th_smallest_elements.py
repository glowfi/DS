# https://www.geeksforgeeks.org/problems/sum-of-elements-between-k1th-and-k2th-smallest-elements3133/1 , Easy

# Brute
# T.C. - O(nlog(n))
# S.C  - O(1)


class Solution:
    def sumBetweenTwoKth(self, A, N, K1, K2):
        return sum(sorted(A)[K1 : K2 - 1])


# Optimal
# T.C. - O(nlog(k2))+O(k2)
# S.C  - O(1)

import heapq


class Solution:
    def sumBetweenTwoKth(self, A, N, K1, K2):
        heap = []

        for num in A:
            heapq.heappush(heap, num * -1)
            if len(heap) > K2 - 1:
                heapq.heappop(heap)

        # 4 8 10 12 14 20 22

        sm = 0

        while len(heap) > K1:
            sm += heapq.heappop(heap) * -1

        return sm
