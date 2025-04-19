# https://leetcode.com/problems/k-closest-points-to-origin/ , Medium


# Optimal
# T.C. - O(nlog(k))+O(k)
# S.C  - O(k)

import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            x, y = point
            d = (x**2 + y**2) ** 0.5
            heapq.heappush(heap, [-d, point])
            if len(heap) > k:
                heapq.heappop(heap)

        ans = []

        while heap:
            ans.append(heapq.heappop(heap)[-1])

        return ans
