# https://www.geeksforgeeks.org/problems/bubble-sort/1 , Easy, Basic

# Question
# Given an array, arr[]. Sort the array using bubble sort algorithm.

# Examples :

# Input: arr[] = [4, 1, 3, 9, 7]
# Output: [1, 3, 4, 7, 9]

# Input: arr[] = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Input: arr[] = [1, 2, 3, 4, 5]
# Output: [1, 2, 3, 4, 5]

# Explanation: An array that is already sorted should remain unchanged after applying bubble sort.

# Constraints:
# 1 <= arr.size() <= 10^3
# 1 <= arr[i] <= 10^3


# Optimal
# T.C. - O(N^2)
# S.C  - O(1)

# Intuition
# This algorithms worst,avg time complexity is O(N^2) and best time complexity
# is O(N) when array is already sorted there will be no swaps.This is a stable
# sorting algo.
# In each iteration place the minimum/maximum most element to the end of
# the array making swaps on the go.For example , for ascending order in
# first iteration the most maximum will be placed at last,then next iteration
# 2nd maximum will be placed at 2nd last index like this.


class Solution:
    # Function to sort the array using bubble sort algorithm.
    def bubbleSort(self, arr: list[int]):
        for i in range(
            len(arr) - 1
        ):  # since at last iteration last element will be at its correct place
            did_swap = False
            for j in range(0, len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    did_swap = True

            if not did_swap:  # if array is sorted no swaps will take place
                break
