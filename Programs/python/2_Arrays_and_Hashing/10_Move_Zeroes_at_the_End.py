# https://leetcode.com/problems/move-zeroes , Easy

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
# -^231 <= nums[i] <= 2^31 - 1

# Brute
# T.C. - O(N)
# S.C  - O(N)

# Intuition
# make a copy of the array and
# push non negative values at first


from typing_extensions import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        cp_nums = [0] * len(nums)

        idx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                cp_nums[idx] = nums[i]
                idx += 1

        nums[:] = cp_nums[:]


# Optimal
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# maintain a idx variable which will tell us the postion to insert the
# non zero values,if we encounter a non zero value we swap it with the value
# at that index and we increment one to the index

from typing_extensions import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[idx], nums[i] = nums[i], nums[idx]
                idx += 1
