# https://practice.geeksforgeeks.org/problems/second-largest3735/1,Easy

# Brute
# T.C. -> O(n*log(n))+O(n)
# S.C. -> O(n)


class Solution:
    def print2largest(self, arr, n):
        arr.sort()

        greatest = arr[-1]
        idx = len(arr) - 1

        while True and idx >= 0:
            if arr[idx] != greatest:
                break
            idx -= 1

        if idx < 0:
            return -1
        return arr[idx]


# Better
# T.C. -> O(n)+O(n)
# S.C. -> O(1)


class Solution:
    def print2largest(self, arr, n):
        large = float("-inf")

        for i in range(len(arr)):
            if arr[i] > large:
                large = arr[i]

        secLarge = -1
        for i in range(len(arr)):
            if arr[i] != large and arr[i] > secLarge:
                secLarge = arr[i]

        return secLarge


# Optimal
# T.C. -> O(n)
# S.C. -> O(1)


class Solution:
    def print2largest(self, arr, n):
        large = arr[0]
        secLarge = -1

        for i in range(1, len(arr)):
            if arr[i] > large:
                secLarge = large
                large = arr[i]
            elif arr[i] < large and arr[i] > secLarge:
                secLarge = arr[i]

        return secLarge
