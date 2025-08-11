# https://leetcode.com/problems/maximum-sum-circular-subarray, Medium, KadanesAlgo

# Question
# Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

# A circular array means the end of the array connects to the beginning of the array. Formally,
# the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

# A subarray may only include each element of the fixed buffer nums at most once. Formally, for a
# subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

# Example 1:

# Input: nums = [1,-2,3,-2]
# Output: 3
# Explanation: Subarray [3] has maximum sum 3.
# Example 2:

# Input: nums = [5,-3,5]
# Output: 10
# Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
# Example 3:

# Input: nums = [-3,-2,-3]
# Output: -2
# Explanation: Subarray [-2] has maximum sum -2.


# Constraints:

# n == nums.length
# 1 <= n <= 3 * 10^4
# -3 * 10^4 <= nums[i] <= 3 * 10^4

# Brute
# T.C. - O(N^2)
# S.C  - O(1)

# Intuition
# generate all subarrays
# find the max from those subarrays

import sys
from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        mx_sum = -sys.maxsize
        n = len(nums)
        for i in range(n):
            sm = 0
            for j in range(n):
                idx = (i + j) % n
                sm += nums[idx]
                mx_sum = max(sm, mx_sum)

        return mx_sum


# Brute
# T.C. - O(N^2)
# S.C  - O(1)

# Intuition
# rotate the array by one
# find max sum subarray
# keep track of global sum subarray

import sys
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        global_sum = -sys.maxsize

        for i in range(len(nums)):
            curr_sum += nums[i]

            if curr_sum > global_sum:
                global_sum = curr_sum

            if curr_sum < 0:
                curr_sum = 0

        return global_sum

    def rotateByOne(self, nums: list[int]) -> None:
        for i in range(len(nums) - 1):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        mx_sum = -sys.maxsize

        for _ in range(len(nums)):
            self.rotateByOne(nums)
            mx_sum = max(mx_sum, self.maxSubArray(nums))

        return mx_sum


# Optimal
# T.C. -
# S.C  - O(1)

# Intuition
# Suppose consider the below array
# a b c d e f g h i j k l m
# ------- --------- -------
#  max-sum min-sum(b) max-sum(a)
# -------------------------- total-sum(s)
# proof -> We know that a+b = S
# we are claiming that b is the min sum
# but suppose we say that in order to make b
# the min sum, we need to reduce the value of b
# if we are reducing the value of b then we have
# to increase the value of a to inorder to balance
# out the sum , but wait a is already max sum we cannot
# increase its value , so by contradiction its proven right
# that b is the min sum
# but whenever my total sum and min-sum is the same, then return
# the normal sum , Egde case [-1,-2,-3] here the circular sum
# becomes 0

import sys
from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_sum = 0

        curr_min_sum = 0
        min_sum = sys.maxsize

        curr_max_sum = 0
        max_sum = -sys.maxsize

        for i in range(len(nums)):
            total_sum += nums[i]

            curr_min_sum = min(nums[i], curr_min_sum + nums[i])
            min_sum = min(min_sum, curr_min_sum)

            curr_max_sum = max(nums[i], curr_max_sum + nums[i])
            max_sum = max(max_sum, curr_max_sum)

        circular_sum = total_sum - min_sum

        if total_sum == min_sum:
            return max_sum

        return max(circular_sum, max_sum)
