# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/?envType=study-plan-v2&envId=top-interview-150 , Medium

# Brute
# T.C. - O(m*nlog(k))
# S.C  - O(k)

import heapq
from typing import List


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:

        max_heap = []
        ans = []

        for num1 in nums1:
            for num2 in nums2:
                sm = -1 * (num1 + num2)
                if len(max_heap) < k:
                    heapq.heappush(max_heap, [sm, num1, num2])
                else:
                    if -sm < -max_heap[0][0]:
                        heapq.heappop(max_heap)
                        heapq.heappush(max_heap, [sm, num1, num2])

        while max_heap:
            _, a, b = heapq.heappop(max_heap)
            ans.append([a, b])

        return ans


# Better
# T.C. - O(m*nlog(k))
# S.C  - O(k)

import heapq
from typing import List


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:

        max_heap = []
        ans = []

        for num1 in nums1:
            for num2 in nums2:
                sm = -1 * (num1 + num2)
                if len(max_heap) < k:
                    heapq.heappush(max_heap, [sm, num1, num2])
                elif -sm < -max_heap[0][0]:
                    heapq.heappop(max_heap)
                    heapq.heappush(max_heap, [sm, num1, num2])
                else:
                    break

        while max_heap:
            _, a, b = heapq.heappop(max_heap)
            ans.append([a, b])

        return ans


# Optimal
# T.C. - O(k log k)
# S.C  - O(K)

# Use a min-heap to track the next minimal sum.
# This approach mimics Dijkstra-style expansion — always greedy, always efficient.

# Intuition
# since 2 arrays are sorted we are sure that 0,0 can be the part of our answer
# we start by inserting the element at 0,0
# we min heap to track the min sum till now

# The next pair with a sum that is just greater than (or equal to) the sum of the previous pair
# would be formed by selecting either the first element of nums1 and the second element of
# nums2, (0, 1), or the second element of nums1 and the first element of nums2, (1, 0),
# whichever has smaller sum. We only need to look at these two pairs because the sum of
# all the other pairs will be greater than this pair.

import heapq


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        ans = []
        visited = set()

        min_heap = []
        heapq.heappush(min_heap, [nums1[0] + nums2[1], 0, 0])
        visited.add((0, 0))

        while len(ans) < k and min_heap:
            sm, i, j = heapq.heappop(min_heap)
            ans.append([nums1[i], nums2[j]])

            # i,j+1
            if j + 1 < len(nums2) and (i, j + 1) not in visited:
                visited.add((i, j + 1))
                heapq.heappush(min_heap, [nums1[i] + nums2[j + 1], i, j + 1])

            # i+1,j
            if i + 1 < len(nums1) and (i + 1, j) not in visited:
                visited.add((i + 1, j))
                heapq.heappush(min_heap, [nums1[i + 1] + nums2[j], i + 1, j])

        return ans
