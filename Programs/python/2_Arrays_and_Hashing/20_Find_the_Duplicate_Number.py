# https://leetcode.com/problems/find-the-duplicate-number , Medium

# Question
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and using only constant extra space.


# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:

# Input: nums = [3,1,3,4,2]
# Output: 3
# Example 3:

# Input: nums = [3,3,3,3,3]
# Output: 3


# Constraints:

# 1 <= n <= 10^5
# nums.length == n + 1
# 1 <= nums[i] <= n
# All the integers in nums appear only once except for precisely one integer which appears two or more times.


# Follow up:

# How can we prove that at least one duplicate number must exist in nums?
# Can you solve the problem in linear runtime complexity?

# Brute
# T.C. - O(N)
# S.C  - O(N)

# Intuition
# Use a hasmap to keep track of seen elements
# if we see a elements more than twice return that element


from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = {}

        for i in nums:
            if i in seen:
                return i
            seen[i] = True

        return -1


# Optimal
# T.C. - O(2N) ~ O(N)
# S.C  - O(1)

# Intuition
# Use the cylic sort algoritm
# sort the array using cyclic sort
# the first number not at its correct place is the duplicate


from typing import List


class Solution:
    def cyclic_sort(self, nums: List[int]) -> None:
        i = 0
        while i < len(nums):
            actualPos = nums[i] - 1
            if nums[actualPos] != nums[i]:
                nums[i], nums[actualPos] = nums[actualPos], nums[i]
            else:
                i += 1

    def findDuplicate(self, nums: List[int]) -> int:
        self.cyclic_sort(nums)

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return nums[i]

        return -1
