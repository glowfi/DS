# https://leetcode.com/problems/subarray-sum-equals-k, Medium, SubarraySumCount

# Question
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.


# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2


# Constraints:

# 1 <= nums.length <= 2 * 10^4
# -1000 <= nums[i] <= 1000
# -10^7 <= k <= 10^7

# Brute
# T.C. - O(N^2)
# S.C  - O(1)

# Intuition
# Generate all subarrays and count
# subarrays with sum k


from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c = 0

        for i in range(len(nums)):
            sm = 0
            for j in range(i, len(nums)):
                sm += nums[j]

                if sm == k:
                    c += 1

        return c


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
# to take a map and store the count till
# that ith index if we are able to find a sum
# s-k that we have seen earlier we can say that
# we have got a subarray with k sum
# Use the concept of prefix sum
# how many s-k we have to remove inorder from curr sum to get k
# no of s-k will be equivalent to no of k

# Now, there may exist multiple subarrays with the prefix sum x-k. So, the number of subarrays
# with sum k that we can generate from the entire subarray ending at index i, is exactly equal
# to the number of subarrays with the prefix sum x-k, that we can remove from the entire subarray.


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sm = 0
        k_sum_count_map = {0: 1}
        count = 0

        for i in range(len(nums)):
            sm += nums[i]

            diff = sm - k

            if diff in k_sum_count_map:
                count += k_sum_count_map[diff]

            if sm not in k_sum_count_map:
                k_sum_count_map[sm] = 1
            else:
                k_sum_count_map[sm] += 1

        return count
