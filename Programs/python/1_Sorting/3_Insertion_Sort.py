# https://www.geeksforgeeks.org/problems/insertion-sort/0 , Easy, Basic

# Question
# The task is to complete the insertsort() function which is used to implement Insertion Sort.

# Examples:

# Input: arr[] = [4, 1, 3, 9, 7]
# Output: [1, 3, 4, 7, 9]
# Explanation: The sorted array will be [1, 3, 4, 7, 9].

# Input: arr[] = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Explanation: The sorted array will be [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].

# Input: arr[] = [4, 1, 9]
# Output: [1, 4, 9]
# Explanation: The sorted array will be [1, 4, 9].

# Constraints:
# 1 <= arr.size() <= 1000
# 1 <= arr[i] <= 1000


# Optimal
# T.C. - O(N^2)
# S.C  - O(1)

# Intuition
# This algorithms worst,avg time complexity is O(N^2) and best time complexity
# is O(N) when array is already sorted there will be no swaps.
# This is a stable sorting algo.
# In this algorithm in every pass we try to place the
# number at its correct position,from the current position
# in which the number is in we try to check with its left
# neighbours whether its lesser than its left neighbour,
# if its lesser than its left neighbour we swap places
# we keep doing it unitl its placed in its correct place


class Solution:
    def insertionSort(self, arr: list[int]):
        # we start from 1 index as 1 does not have any left neighbours
        for i in range(1, len(arr)):
            j = i
            while j > 0 and arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                j -= 1

        return arr
