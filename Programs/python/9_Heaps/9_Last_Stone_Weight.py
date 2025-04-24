# https://leetcode.com/problems/last-stone-weight/ , Easy


# Brute
# T.C. - O(n log n) + O(n^2) = O(n^2)
# S.C  - O(1)

import bisect


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()

        while len(stones) > 1:
            first, second = stones.pop(-1), stones.pop(-1)
            if first != second:
                diff = first - second
                best_pos_to_insert = bisect.bisect_left(stones, diff)
                stones.insert(best_pos_to_insert, diff)

        if not stones:
            return 0
        return stones[0]


# Optimal
# T.C. - O(nlog(n))
# S.C  - O(n)

import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        heap = []
        for num in stones:
            heapq.heappush(heap, num * -1)

        while len(heap) > 1:
            first, second = heapq.heappop(heap) * -1, heapq.heappop(heap) * -1
            if first != second:
                heapq.heappush(heap, (first - second) * -1)

        if not heap:
            return 0
        return heap[0] * -1
