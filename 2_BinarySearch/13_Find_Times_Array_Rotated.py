# https://practice.geeksforgeeks.org/problems/rotation4723/1,Medium


# Find Index of minimum element

# Brute
# T.C. -> O(n)
# S.C. -> O(1)


class Solution:
    def findKRotation(self, arr, n):
        # Array not rotated
        if arr[0] < arr[-1]:
            return 0

        times = 0
        mn = float("inf")

        for idx in range(n):
            if arr[idx] < mn:
                mn = arr[idx]
                times = idx

        return times


# Optimal
# T.C. -> O(log(n))
# S.C. -> O(1)


class Solution:
    def findKRotation(self, arr, n):
        if arr[0] < arr[-1]:
            return 0

        st, en = 1, n - 2

        while st <= en:
            mid = st + (en - st) // 2

            if arr[mid] < arr[mid - 1] and arr[mid] < arr[mid + 1]:
                return mid

            # Right half is sorted
            if arr[mid] < arr[en]:
                en = mid - 1

            # Left half is sorted
            else:
                st = mid + 1

        if arr[0] < arr[n - 1]:
            return 0
        return n - 1
