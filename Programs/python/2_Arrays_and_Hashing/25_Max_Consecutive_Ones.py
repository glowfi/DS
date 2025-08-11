# https://leetcode.com/problems/max-consecutive-ones, Medium, Basic

# Question
# Given a binary array nums, return the maximum number of consecutive 1's in the array.


# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:

# Input: nums = [1,0,1,1,0,1]
# Output: 2


# Constraints:

# 1 <= nums.length <= 10^5
# nums[i] is either 0 or 1.


# Optimal
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# Keep track of number of 1s encountered till now
# if current num is 1 increment 1s encountered
# at every step you encounter 1 find max of count and max_ones
# if current num is 0 reset counter


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        c = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                c += 1
                max_ones = max(max_ones, c)
            else:
                c = 0

        return max_ones
