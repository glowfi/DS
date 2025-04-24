# https://leetcode.com/problems/kth-largest-element-in-a-stream , Easy


# Optimal
# T.C. - O(log(n))
# S.C  - O(1)

import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.heap = []
        self.k = k

        for num in nums:
            self.maintainHeapOfKLength(num)

    def maintainHeapOfKLength(self, val: int):
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        self.maintainHeapOfKLength(val)
        return self.heap[0]
