# https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1, Medium, Prefix Sum + HashMap

# Question
# Given an array arr[] containing integers and an integer k, your task is to find the length of the longest subarray where the sum of its elements is equal to the given value k. If there is no subarray with sum equal to k, return 0.

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
# T.C. - O(n^2)
# S.C  - O(1)

# Intuition
# Generate all pssible subarrays
# Find the longeest subarray with
# sum k


from typing import List


class Solution:
    def longestSubarray(self, arr: List[int], k: int):
        longest = 0

        for i in range(len(arr)):
            sm = 0
            for j in range(i, len(arr)):
                sm += arr[j]
                if sm == k:
                    longest = max(longest, j - i + 1)

        return longest


# Optimal
# T.C. - O(n)
# S.C  - O(n)

# Intuition
# We use the concept of prefix sum but
# now we store the index as close to left
# as possible to increase the subarray size

from typing import List


class Solution:
    def longestSubarray(self, arr: List[int], k: int):
        curr_pref_sum = 0
        idx_mp = {0: -1}
        longest = 0

        for idx, num in enumerate(arr):
            curr_pref_sum += num
            complement = curr_pref_sum - k

            if complement in idx_mp:
                longest = max(longest, idx - idx_mp[complement])

            # store the index as left as possible as newer index will decrease our size
            if curr_pref_sum not in idx_mp:
                idx_mp[curr_pref_sum] = idx

        return longest
