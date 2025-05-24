# https://leetcode.com/problems/maximum-subarray , Medium

# Question
# Given an integer array nums, find the subarray with the largest sum, and return its sum.


# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.


# Constraints:

# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4


# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

# Brute
# T.C. - O(N^2)
# S.C  - O(1)

# Intuition
# Generate all subarrays, and find the subarray
# with max sum


from typing import List
import sys


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx_sum = -sys.maxsize
        for i in range(len(nums)):
            sm = 0
            for j in range(i, len(nums)):
                sm += nums[j]
                mx_sum = max(mx_sum, sm)

        return mx_sum


# Optimal
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# A subarray with a sum less than 0 will always reduce our answer and
# so this type of subarray cannot be a part of the subarray with maximum sum
# among all the sum calculated we take the sum.
# In each pass we decide whethet to start a new seqeunce or continue or our
# old seqeunce

from typing import List
import sys


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


# Optimal
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# print the sequence
# when the sum is zero we can say right its a start of the sequnce
# take 2 pointers ansStart and ansEnd and another variable to track
# current start


from typing import List
import sys


class Solution:
    def maxSubArray(self, nums: List[int]):
        curr_sum = 0
        global_sum = -sys.maxsize
        resStart, resEnd = 0, 0
        currStart = 0

        for i in range(len(nums)):
            if curr_sum == 0:
                currStart = i

            curr_sum += nums[i]

            if curr_sum > global_sum:
                global_sum = curr_sum
                resStart = currStart
                resEnd = i

            if curr_sum < 0:
                curr_sum = 0

        print("Maximum subarray sequence:", nums[resStart : resEnd + 1])
        print("Maximum subarray sum:", global_sum)


obj = Solution()
ls = [1, -2, -1, 0, 3, 4]
ls = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
obj.maxSubArray(ls)
