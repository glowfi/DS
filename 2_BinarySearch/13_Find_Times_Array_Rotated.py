# https://practice.geeksforgeeks.org/problems/rotation4723/1,Medium


# Find Index of minimum element

# Brute
# T.C. -> O(n)
# S.C. -> O(1)


class Solution:
    def findKRotation(self, arr, n):
        mn = float("inf")
        idx = -1

        for i in range(len(arr)):
            if arr[i] < mn:
                mn = arr[i]
                idx = i
        return idx


# Optimal
# T.C. -> O(log(n))
# S.C. -> O(1)


class Solution(object):
    def findKRotation(self, arr, n):
        st, en = 0, len(arr) - 1
        N = len(arr)

        while st <= en:
            mid = (st + en) // 2

            prev = (mid + N - 1) % N
            nxt = (mid + 1) % N

            # Minimum element is smaller than both of its neighbour
            if arr[mid] <= arr[prev] and arr[mid] <= arr[nxt]:
                return mid

            # Identify Unsorted part as minimum element will always lie there (By observation)

            # Right is Unsorted
            elif arr[mid] >= arr[en]:
                st = mid + 1

            else:
                en = mid - 1
