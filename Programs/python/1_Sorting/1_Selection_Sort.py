# https://www.geeksforgeeks.org/problems/selection-sort/1, Easy, Basic

# Question
# Given an array arr, use selection sort to sort arr[] in increasing order.

# Examples :

# Input: arr[] = [4, 1, 3, 9, 7]
# Output: [1, 3, 4, 7, 9]
# Explanation: Maintain sorted (in bold) and unsorted subarrays.
# Select 1. Array becomes 1 4 3 9 7.
# Select 3.  Array becomes 1 3 4 9 7.
# Select 4. Array becomes 1 3 4 9 7.
# Select 7. Array becomes 1 3 4 7 9.
# Select 9. Array becomes 1 3 4 7 9.

# Input: arr[] = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Input: arr[] = [38, 31, 20, 14, 30]
# Output: [14, 20, 30, 31, 38]

# Constraints:
# 1 ≤ arr.size() ≤ 10^3
# 1 ≤ arr[i] ≤ 10^6


# Optimal
# T.C. - O(N^2)
# S.C  - O(1)

# Intuition
# This is an unstable sorting algorithm but can be made stable to maintain relative
# ordering of element but will increase time complexity.
# This algorithms worst,best,avg time complexity is O(N^2)
# In each iteration place the minimum/maximum most element to its correct place.
# For example for ascending in 1st iteration place the most minimum to 0th index
# , next iteration 2nd minimum to 1st index like this.


class Solution:
    def selectionSort(self, arr: list[int]):
        for i in range(len(arr)):
            min_idx = i
            for j in range(i, len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
