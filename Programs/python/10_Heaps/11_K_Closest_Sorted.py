# https://leetcode.com/problems/find-k-closest-elements , Medium

# Brute
# T.C. -  O(nlog(n))+O(nlog(k))
# S.C  - O(1)


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # First, sort the array based on the absolute difference with x
        sorted_arr = sorted(arr, key=lambda num: abs(num - x))

        # Select the k closest elements
        closest_k = sorted_arr[:k]

        # Sort the k closest elements in ascending order
        result = sorted(closest_k)

        return result


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
                heapq.heappush(max_heap, [abs(x - num) * -1, num])
            else:
                if abs(x - num) < -max_heap[0][0]:
                    heapq.heappush(max_heap, [abs(x - num) * -1, num])
                    heapq.heappop(max_heap)

        ans = []
        while max_heap:
            ans.append(heapq.heappop(max_heap)[-1])

        return sorted(ans)


# Optimal
# T.C. -  O(log N) + O(k)
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
        idx = self.lowerBound(arr, len(arr), x)  # floor can be used with idx,idx+1
        l, r = idx - 1, idx

        while l >= 0 and r < len(arr) and k > 0:
            if abs(arr[l] - x) <= abs(arr[r] - x):
                l -= 1
            else:
                r += 1
            k -= 1

        # Either l or r ends
        while k > 0 and l >= 0:
            l -= 1
            k -= 1

        while k > 0 and r < len(arr):
            r += 1
            k -= 1

        return arr[l + 1 : r]
