# https://www.geeksforgeeks.org/problems/sorting-elements-of-an-array-by-frequency-1587115621/1 , Medium


# Optimal
# T.C. - O(n)+O(nlog(n))+O(n)
# S.C  - O(n)+O(n)+O(n)

import heapq


class Solution:

    def sortByFreq(self, arr):
        ans = [0] * len(arr)

        freq_map = {}

        for num in arr:
            if num not in freq_map:
                freq_map[num] = 1
            else:
                freq_map[num] += 1

        heap = []
        for num, freq in freq_map.items():
            heapq.heappush(heap, [freq * -1, num])

        i = 0
        while heap:
            freq, num = heapq.heappop(heap)
            for _ in range(freq * -1):
                ans[i] = num
                i += 1

        return ans
