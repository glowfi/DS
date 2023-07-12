# https://practice.geeksforgeeks.org/problems/maximum-value-in-a-bitonic-array3001/1, Easy


# Brute
# T.C. -> O(n)
# S.C. -> O(1)


class Solution:
    def findMaximum(self, arr, n):
        if arr[0] > arr[1]:
            return arr[0]

        if arr[n - 1] > arr[n - 2]:
            return arr[n - 1]

        for i in range(1, n):
            if arr[i] > arr[i + 1] and arr[i] > arr[i - 1]:
                return arr[i]
        return -1


# Optimal
# T.C. -> O(log(n))
# S.C. -> O(1)


class Solution:
    def findMaximum(self, arr, n):
        if arr[0] > arr[1]:
            return arr[0]

        if arr[n - 1] > arr[n - 2]:
            return arr[n - 1]

        st, en = 1, n - 2

        while st <= en:
            mid = st + ((en - st) // 2)

            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return arr[mid]

            # Left Neighbour is more Promising
            elif arr[mid - 1] > arr[mid] and arr[mid - 1] > arr[mid + 1]:
                en = mid - 1

            # Right Neighbour is more Promising
            else:
                st = mid + 1

        return -1
