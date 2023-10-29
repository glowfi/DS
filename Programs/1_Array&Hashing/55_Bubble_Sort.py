# https://practice.geeksforgeeks.org/problems/bubble-sort/1 , Easy

# Algorithm
# + Target is to in each place the greatest element to the extreme right position.
# + Inner loop represents n-1 passses. [Last Pass array is already sorted]
# + Outer loop represents swaps where we swap adjacent elements in the unsorted part 0-n-i-1.
#   [We push greatest element to the righ thats why 0-n-i-1 is unsorted at first]

# Iterative
# Brute
# T.C. - O(n^2) [Worst+Average] [Best Case -> O(n) when array is already sorted] [Stable]
# S.C  - O(1)


class Solution:
    def bubbleSort(self, arr, n):
        for i in range(0, n - 1):
            swapped = False
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True

            if not swapped:
                break


# Recursive
# Brute
# T.C. - O(n^2) [Worst+Average] [Best Case -> O(n) when array is already sorted]
# S.C  - O(n) [Recursion stack space]


class Solution:
    def helper(self, i, arr, n):
        if i == n:
            return

        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            return

        self.helper(i + 1, arr, n)

    def bubbleSort(self, arr, n):
        self.helper(0, arr, n)
