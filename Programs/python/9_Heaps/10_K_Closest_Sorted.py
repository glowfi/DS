# https://leetcode.com/problems/find-k-closest-elements , Medium

# Better
# T.C. -  O(log N + k log k)
# S.C  - O(1)


class Solution:
    def lowerBound(self, arr: list[int], n: int, x: int) -> int:
        low = 0
        high = n - 1
        ans = n

        while low <= high:
            mid = (low + high) // 2
            # maybe an answer
            if arr[mid] >= x:
                ans = mid
                # look for smaller index on the left
                high = mid - 1
            else:
                low = mid + 1  # look on the right

        return ans

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = self.lowerBound(arr, len(arr), x)
        l, r = idx - 1, idx
        res = []

        while l >= 0 and r < len(arr) and k > 0:
            if abs(arr[l] - x) <= abs(arr[r] - x):
                res.append(arr[l])
                l -= 1
            else:
                res.append(arr[r])
                r += 1
            k -= 1

        # Either l or r ends
        while k > 0 and l >= 0:
            res.append(arr[l])
            l -= 1
            k -= 1

        while k > 0 and r < len(arr):
            res.append(arr[r])
            r += 1
            k -= 1

        return sorted(res)


# Better
# T.C. - O(nlog(n))+O(klog(k))+O(nlog(n))
# S.C  - O(1)

import heapq


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []

        for i in arr:
            heapq.heappush(heap, [abs(i - x), i])

        res = []
        while k:
            res.append(heapq.heappop(heap)[-1])
            k -= 1

        return sorted(res)


# Better
# T.C. - O(nlog(k))+O(nlog(n))
# S.C  - O(1)

import heapq


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        max_heap = []
        for num in arr:
            if len(max_heap) < k:
                heapq.heappush(max_heap, (-abs(num - x), num))
            else:
                if abs(num - x) < -max_heap[0][0]:
                    heapq.heappop(max_heap)
                    heapq.heappush(max_heap, (-abs(num - x), num))
        return sorted([num for _, num in max_heap])
