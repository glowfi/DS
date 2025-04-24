# https://leetcode.com/problems/kth-largest-element-in-an-array/ , Medium


# Better
# T.C. - O(nlog(n))
# S.C  - O(1)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k - 1]


# Optimal
# T.C. - O(nlog(k))
# S.C  - O(log(n))

import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap: list[int] = []

        for i in range(len(nums)):
            elem = nums[i]
            heapq.heappush(heap, elem)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]


# Optimal [order maintained]
# T.C. - O(nlog(k))
# S.C  - O(log(n))

import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap: list[int] = []

        for i in range(len(nums)):
            elem = nums[i]
            if len(heap) < k:
                heapq.heappush(heap, elem)
            else:
                if elem > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, elem)

        return heap[0]
