# https://practice.geeksforgeeks.org/problems/check-if-an-array-is-sorted0701/1 , Easy

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
# S.C  - O(1)

# Intuition
# Keep checking that current element must be greater than equal to previous element
# if current element lesser than previous element return false


class Solution:
    def arraySortedOrNot(self, arr) -> bool:
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                return False
        return True
