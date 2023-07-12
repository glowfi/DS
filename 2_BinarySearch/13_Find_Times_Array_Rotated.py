# https://practice.geeksforgeeks.org/problems/rotation4723/1,Medium


# Find Index of minimum element

# Brute
# T.C. -> O(n)
# S.C. -> O(1)


class Solution:
    def findKRotation(self, arr, n):
        if arr[0] < arr[-1]:
            return 0

        mn = float("inf")
        K = -1
        for i in range(len(arr)):
            if arr[i] < mn:
                mn = arr[i]
                K = i

        return K


# Optimal
# T.C. -> O(log(n))
# S.C. -> O(1)


class Solution:
    def findKRotation(self, arr, n):
        if arr[0] <= arr[-1]:
            return 0

        K = -1
        st, en = 0, len(arr) - 1
        N = len(arr)

        while st <= en:
            mid = st + ((en - st) // 2)

            prev = (mid + N - 1) % N
            nxt = (mid + 1) % N

            # Minimum elemnt will be in unsorted part (By Observation).Identify the unsorted part.
            if arr[mid] <= arr[prev] and arr[mid] <= arr[nxt]:
                K = mid
                break

            # Right Half is sorted
            elif arr[mid] <= arr[en]:
                en = mid - 1

            # Left Half is sorted
            else:
                st = mid + 1

        return K
