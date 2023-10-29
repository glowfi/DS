# https://practice.geeksforgeeks.org/problems/bubble-sort/1 , Easy

# Algorithm
# + Target is to place the greatest or minimum element in 0th or last place in each iteration.
# + Inner loop represents n-1 passses. [Last Pass array is already sorted]
# + Outer loop represents swaps where we find the index of max or min element and swap in the unsorted part 0-n-i-1.

# Iterative
# Brute
# T.C. - O(n^2) [Worst+Average+Best] [Unstable but can be made stable]
# S.C  - O(1)


class Solution:
    def select(self, arr, i):
        elem = arr[0]
        idx = 0
        n = len(arr)
        for j in range(1, n - i):
            if arr[j] > elem:
                elem = arr[j]
                idx = j
        return idx

    def selectionSort(self, arr, n):
        for i in range(n):
            last = n - i - 1
            idx = self.select(arr, i)
            arr[idx], arr[last] = arr[last], arr[idx]


# Recursive
# Brute
# T.C. - O(n^2) [Worst+Average+Best]
# S.C  - O(n) [Recursion stack space]


class Solution:
    def select(self, arr, i):
        elem = arr[0]
        idx = 0
        n = len(arr)
        for j in range(1, n - i):
            if arr[j] > elem:
                elem = arr[j]
                idx = j
        return idx

    def helper(self, i, arr, n):
        if i == n:
            return
        last = n - i - 1
        idx = self.select(arr, i)
        arr[idx], arr[last] = arr[last], arr[idx]
        self.helper(i + 1, arr, n)

    def selectionSort(self, arr, n):
        self.helper(0, arr, len(arr))
