# https://leetcode.com/problems/move-zeroes, Easy, Two Pointers

# Question
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.


# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]

# Constraints:
# 1 <= nums.length <= 10^4
# -23^1 <= nums[i] <= 2^31 - 1

# Follow up: Could you minimize the total number of operations done?

# Brute
# T.C. - O(n)
# S.C  - O(n)

# Intuition
# Store the non zero elements in an temporary array
# then assign nums to temporary array

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tmp = [0] * len(nums)

        k = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                tmp[k] = nums[i]
                k += 1

        nums[:] = tmp


# Optimal
# T.C. - O(n)
# S.C  - O(1)

# Intuition
# It is clear that all the non zero values are going to lie on left
# and all zero values are going to lie on the right.
# We are going to take two pointers l and r. r will traverse the
# whole array and l will store the index to put the non zero values.
# As we discover non zero values we are going to put the non zero
# values to the l pointer.


from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l, r = 0, 0
        while r < len(nums):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1
