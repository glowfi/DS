# https://practice.geeksforgeeks.org/problems/who-will-win-1587115621/1, Easy, Basic

# Question
# Given an array, arr[] sorted in ascending order and an integer k. Return true if k is present in the array, otherwise, false.

# Examples:

# Input: arr[] = [1, 2, 3, 4, 6], k = 6
# Output: true
# Explanation: Since, 6 is present in the array at index 4 (0-based indexing), output is true.

# Input: arr[] = [1, 2, 4, 5, 6], k = 3
# Output: false
# Explanation: Since, 3 is not present in the array, output is false.

# Input: arr[] = [2, 3, 5, 6], k = 1
# Output: false
# Constraints:
# 1 <= arr.size() <= 10^6
# 1 <= k <= 10^6
# 1 <= arr[i] <= 10^6

# Optimal
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# Traverse the array until you encounter the element you are searching


class Solution:
    def searchInSorted(self, arr: list[int], k: int):
        for i in range(len(arr)):
            if arr[i] == k:
                return True
        return False
