# https://www.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1 , Medium, LongestSubarraySum

# Question
# Given an array arr containing both positive and negative integers, the task is to compute the length of the largest subarray that has a sum of 0.

# Examples:

# Input: arr[] = [15, -2, 2, -8, 1, 7, 10, 23]
# Output: 5
# Explanation: The largest subarray with a sum of 0 is [-2, 2, -8, 1, 7].

# Input: arr[] = [2, 10, 4]
# Output: 0
# Explanation: There is no subarray with a sum of 0.

# Input: arr[] = [1, 0, -4, 3, 1, 0]
# Output: 5
# Explanation: The subarray is [0, -4, 3, 1, 0].

# Constraints:
# 1 ≤ arr.size() ≤ 10^6
# −10^3 ≤ arr[i] ≤ 10^3, for each valid i

# Brute
# T.C. - O(N^2)
# S.C  - O(1)

# Intuition
# Generate all subarrays
# find the longest subarray with 0 sum from them


class Solution:
    def maxLen(self, arr: list[int]) -> int:
        mx_len = 0
        for i in range(len(arr)):
            sm = 0
            for j in range(i, len(arr)):
                sm += arr[j]
                if sm == 0:
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
    def maxLen(self, arr: list[int]) -> int:
        sm = 0
        k = 0

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
