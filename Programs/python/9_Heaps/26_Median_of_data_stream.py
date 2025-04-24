# https://leetcode.com/problems/find-median-from-data-stream/ , Hard

# Brute
# T.C. - addnum(O(log(n))+O(n)) , findMedian (O(1))
# S.C  - O(1)

from bisect import bisect_left


class MedianFinder:

    def __init__(self):
        self.stream: list[int] = []

    def addNum(self, num: int) -> None:
        idx = bisect_left(self.stream, num)
        self.stream.insert(idx, num)

    def findMedian(self) -> float:
        mid = len(self.stream) // 2

        if len(self.stream) % 2 == 0:
            return (self.stream[mid] + self.stream[mid - 1]) / 2
        return self.stream[mid]


# Optimal
# T.C. -
# S.C  -


# Left will be a max heap
# Right will be a min heap
# we want max from left and min from right for finding median
# if we have odd size array either the left or right can have one extra element
# we need to make sure the diff of size between 2 array must be <=1
# element coming to use gets placed to left if its smaller than lefts top
# element coming to use gets placed to right if its greater than lefts top
# After pushing try maintaing the property of diff 1

import heapq


class MedianFinder:

    def __init__(self):
        self.left_max_heap = []
        self.right_min_heap = []

    def addNum(self, num: int) -> None:
        # Put element
        if not self.left_max_heap or num < -self.left_max_heap[0]:
            heapq.heappush(self.left_max_heap, -num)
        else:
            heapq.heappush(self.right_min_heap, num)

        # Maintain diff
        if len(self.left_max_heap) - len(self.right_min_heap) > 1:
            heapq.heappush(self.right_min_heap, -heapq.heappop(self.left_max_heap))
        elif len(self.left_max_heap) < len(self.right_min_heap):
            heapq.heappush(self.left_max_heap, -heapq.heappop(self.right_min_heap))

    def findMedian(self) -> float:
        # if even
        n = len(self.left_max_heap) + len(self.right_min_heap)
        if n % 2 == 0:
            a, b = -self.left_max_heap[0], self.right_min_heap[0]
            return (a + b) / 2
        return -self.left_max_heap[0]
