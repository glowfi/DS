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
# All non-zero elements should end up on the left side of the array, and all zeros on the right,
# while keeping the relative order of non-zero elements the same.
#
# To do this, think of one pointer as a “write” pointer that marks the position where
# the next non-zero element should go, and another pointer as a “scan” pointer that
# moves through the array. As we scan, whenever we see a non-zero value, we swap it into
# the position of the write pointer and move the write pointer forward. Zeros are simply skipped.
#
# For example, in [0, 1, 0, 3, 12]:
#
# Scan hits 1: swap with first position → [1, 0, 0, 3, 12]
# Scan hits 3: put it next → [1, 3, 0, 0, 12]
# Scan hits 12: put it next → [1, 3, 12, 0, 0]
# By the end, all non-zeros are compacted at the front in their original order, and zeros naturally move to the back.


from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        p1, p2 = 0, 0
        while p2 < len(nums):
            if nums[p2] != 0:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1
            p2 += 1
