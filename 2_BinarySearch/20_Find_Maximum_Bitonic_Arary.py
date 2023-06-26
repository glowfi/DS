# https://practice.geeksforgeeks.org/problems/maximum-value-in-a-bitonic-array3001/1, Easy

# Optimal
# T.C. -> O(log(n))
# S.C. -> O(1)


class Solution:
    def findMaximum(self, arr, n):
        if len(arr) == 1:
            return arr[0]

        st, en = 0, len(arr) - 1

        while st <= en:
            mid = (st + en) // 2

            if mid > 0 and mid < n - 1:
                if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                    return arr[mid]

                # Left is Promising
                elif arr[mid - 1] > arr[mid]:
                    en = mid - 1
                # Right is Promising
                else:
                    st = mid + 1

            elif mid == 0:
                if arr[0] > arr[1]:
                    return arr[0]
                return arr[1]

            elif mid == len(arr) - 1:
                if arr[n - 1] > arr[n - 2]:
                    return arr[n - 1]
                return arr[n - 2]
