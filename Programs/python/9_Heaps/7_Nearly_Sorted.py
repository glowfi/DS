# https://www.geeksforgeeks.org/problems/nearly-sorted-1587115620/1 , Medium

# Brute
# T.C. - O(n*k)
# S.C  - O(1)


class Solution:
    def nearlySorted(self, arr, k):
        for i in range(1, len(arr)):
            j = i
            while j > 0 and arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                j -= 1


# Better
# T.C. - O(nlog(n))
# S.C  - O(1)


class Solution:
    def nearlySorted(self, arr, k):
        arr.sort()


# Optimal [Min heap]
# T.C. - O(nlog(k))
# S.C  - O(k)

# Draw all possibilities set and you will at every idx for final sorted array we find min from k+1 elements

import heapq


class Solution:
    def nearlySorted(self, arr, k):
        heap = []
        idx = 0
        for num in arr:
            heapq.heappush(heap, num)
            if len(heap) > k + 1:
                res = heapq.heappop(heap)
                arr[idx] = res
                idx += 1
        while heap:
            arr[idx] = heapq.heappop(heap)
            idx += 1
