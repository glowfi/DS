# https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1 , Medium, LongestSubarraySum

# Question
# Given an array arr[] containing integers and an integer k, your task is to find the
# length of the longest subarray where the sum of its elements is equal to the given value k. If there is no subarray with sum equal to k, return 0.

# Examples:

# Input: arr[] = [10, 5, 2, 7, 1, -10], k = 15
# Output: 6
# Explanation: Subarrays with sum = 15 are [5, 2, 7, 1], [10, 5] and [10, 5, 2, 7, 1, -10]. The length of the longest subarray with a sum of 15 is 6.

# Input: arr[] = [-5, 8, -14, 2, 4, 12], k = -5
# Output: 5
# Explanation: Only subarray with sum = -5 is [-5, 8, -14, 2, 4] of length 5.

# Input: arr[] = [10, -10, 20, 30], k = 5
# Output: 0
# Explanation: No subarray with sum = 5 is present in arr[].

# Constraints:
# 1 ≤ arr.size() ≤ 10^5
# -10^4 ≤ arr[i] ≤ 10^4
# -10^9 ≤ k ≤ 10^9

# Brute
# T.C. - O(N^2)
# S.C  - O(1)

# Intuition
# Generate all subarrays
# find the longest subarray with k sum from them


class Solution:
    def longestSubarray(self, arr: list[int], k: int) -> int:
        # code here
        mx_len = 0
        for i in range(len(arr)):
            sm = 0
            for j in range(i, len(arr)):
                sm += arr[j]
                if sm == k:
                    mx_len = max(mx_len, j - i + 1)

        return mx_len


# Optimal
# T.C. - O(N)
# S.C  - O(N)

# Intuition
# Suppose i have an array below :
#  x    k
# --- -----
# a b c d e f g h
# ---------
#     s

# s is the sum till now
# we are looking for subarray with k sum ,
# if k sum is already present then k+x will
# give us "s" , so in every pass we are going
# to take a map and store the prefix sum till
# that ith index if we are able to find a sum
# s-k that we have seen earlier we can say that
# we have got a subarray with k sum , current_i-mp[s-k]
# will give the current length
# Use the concept of prefix sum


class Solution:
    def longestSubarray(self, arr: list[int], k: int) -> int:
        sm = 0
        pref_sum_map = {0: -1}  # at first the size is -1
        mx_len = 0

        for i in range(len(arr)):
            sm += arr[i]

            diff = sm - k

            if diff in pref_sum_map:
                mx_len = max(mx_len, i - pref_sum_map[diff])

            if (
                sm not in pref_sum_map
            ):  # store the index as left as possible as newer index will decrease our size
                pref_sum_map[sm] = i

        return mx_len
