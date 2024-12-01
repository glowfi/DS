# https://practice.geeksforgeeks.org/problems/check-if-an-array-is-sorted0701/1,Easy

# Brute
# T.C. -> O(nlog(n))
# S.C. -> O(n)


class Solution:
    def arraySortedOrNot(self, arr, n):
        return arr == sorted(arr)


# Optimal
# T.C. -> O(n)
# S.C. -> O(1)


class Solution:
    def arraySortedOrNot(self, arr, n):
        for i in range(1, len(arr)):
            if arr[i - 1] <= arr[i]:
                continue
            else:
                return False
        return True
