# https://leetcode.com/problems/rotate-array, Medium, Reverse / Cyclic Shift

# Question
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# Example 2:
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]


# Constraints:
# 1 <= nums.length <= 10^5
# -2^31 <= nums[i] <= 2^31 - 1
# 0 <= k <= 10^5


# Follow up:
# Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
# Could you do it in-place with O(1) extra space?

# Brute
# T.C. - O(n*k)
# S.C  - O(1)

# Intuition
# Right rotate the array k times

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            for j in range(len(nums) - 1, 0, -1):
                nums[j], nums[j - 1] = nums[j - 1], nums[j]


# Optimal
# T.C. - O(n)+O(n)+O(n) ~ O(n)
# S.C  - O(1)

# Intuition
# Reverse the entire array
# Reverse the array from 0 to k-1
# Reverse the array from k to n-1

from typing import List


class Solution:
    def rev_array(self, i: int, j: int, ls: list[int]):
        while i < j:
            ls[i], ls[j] = ls[j], ls[i]
            i += 1
            j -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        self.rev_array(0, n - 1, nums)
        self.rev_array(0, k - 1, nums)
        self.rev_array(k, n - 1, nums)
