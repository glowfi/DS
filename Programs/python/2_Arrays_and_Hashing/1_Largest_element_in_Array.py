# https://practice.geeksforgeeks.org/problems/largest-element-in-array4009/1 , Easy

# Question
# Given an array arr[]. The task is to find the largest element and return it.

# Examples:

# Input: arr[] = [1, 8, 7, 56, 90]
# Output: 90
# Explanation: The largest element of the given array is 90.

# Input: arr[] = [5, 5, 5, 5]
# Output: 5
# Explanation: The largest element of the given array is 5.

# Input: arr[] = [10]
# Output: 10
# Explanation: There is only one element which is the largest.

# Constraints:
# 1 <= arr.size()<= 10^6
# 0 <= arr[i] <= 10^6

# Brute
# T.C. - O(Nlog(N))
# S.C  - O(1)

# Intuition
# Sort the array in descending order to get largest
# element at index 0


class Solution:
    def largest(self, arr: list[int]) -> int:
        return sorted(arr, reverse=True)[0]


# Optimal
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# traverse the entire array to find the max element


class Solution:
    def largest(self, arr: list[int]) -> int:
        max_element = arr[0]

        for i in range(1, len(arr)):
            if arr[i] > max_element:
                max_element = arr[i]

        return max_element
