# https://www.geeksforgeeks.org/problems/check-if-an-array-is-sorted0701/1 , Easy, IBH

# Question
# Given an array arr[], check whether it is sorted in non-decreasing order. Return true if it is sorted otherwise false.

# Examples:

# Input: arr[] = [10, 20, 30, 40, 50]
# Output: true
# Explanation: The given array is sorted.

# Input: arr[] = [90, 80, 100, 70, 40, 30]
# Output: false
# Explanation: The given array is not sorted.

# Constraints:
# 1 ≤ arr.size ≤ 10^6
# - 10^9 ≤ arr[i] ≤ 10^9


# Optimal
# T.C. - O(N)
# S.C  - O(N) [recursion stack space]

# Intuition
# Use IBH method to solve this problem
# Assum that the given function will tell you whether array is sorted or not from
# i+1 to nth position (hypothesis),if array is sorted from i+1 position then we just
# need to check if the i+1 element is greater than current element or not


class Solution:
    def isSorted(self, arr: list[int]) -> bool:
        def helper(idx: int, arr: list[int]) -> bool:
            # Base Case
            if idx == len(arr) - 1:
                return True

            # Hypo
            isSorted = helper(idx + 1, arr)

            # Induction
            if not isSorted:
                return False

            if idx < len(arr) and arr[idx + 1] < arr[idx]:
                return False

            return True

        return helper(0, arr)
