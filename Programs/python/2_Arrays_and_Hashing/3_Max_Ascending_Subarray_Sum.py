# https://leetcode.com/problems/maximum-ascending-subarray-sum, Easy, Basic

# Question
# Given an array of positive integers nums, return the maximum possible sum of an strictly increasing subarray in nums.

# A subarray is defined as a contiguous sequence of numbers in an array.


# Example 1:

# Input: nums = [10,20,30,5,10,50]
# Output: 65
# Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.
# Example 2:

# Input: nums = [10,20,30,40,50]
# Output: 150
# Explanation: [10,20,30,40,50] is the ascending subarray with the maximum sum of 150.
# Example 3:

# Input: nums = [12,17,15,13,10,11,12]
# Output: 33
# Explanation: [10,11,12] is the ascending subarray with the maximum sum of 33.


# Constraints:

# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100


# Optimal
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# Keep track of curr_sum and max_sum
# whenever a peak drop comes update max_sum
# keep adding to curr_sum


from typing import List
import sys


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = -sys.maxsize
        curr_sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                max_sum = max(curr_sum, max_sum)
                curr_sum = nums[i]
            else:
                curr_sum += nums[i]

        max_sum = max(curr_sum, max_sum)

        return max_sum
