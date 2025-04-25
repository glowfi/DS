# https://www.geeksforgeeks.org/problems/replace-elements-by-its-rank-in-the-array/1 , Easy


# Optimal
# T.C. - O(nlog(n))+O(nlog(n))
# S.C  - O(n)

import heapq


class Solution:
    def replaceWithRank(self, N, arr):
        heap = []

        for idx, num in enumerate(arr):
            heapq.heappush(heap, [num, idx])

        rank = 1
        prev_num = -1
        while heap:
            num, idx = heapq.heappop(heap)

            if num != prev_num and prev_num != -1:
                rank += 1
            arr[idx] = rank
            prev_num = num

        return arr
