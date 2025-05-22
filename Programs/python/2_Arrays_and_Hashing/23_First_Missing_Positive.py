# https://leetcode.com/problems/first-missing-positive , Hard

# Question
# Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.


# Example 1:

# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.
# Example 2:

# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.
# Example 3:

# Input: nums = [7,8,9,11,12]
# Output: 1
# Explanation: The smallest positive integer 1 is missing.


# Constraints:

# 1 <= nums.length <= 10^5
# -2^31 <= nums[i] <= 2^31 - 1

# Brute
# T.C. - O(max*N)
# S.C  - O(1)

# Intuition
# we know that all the positive numbers will lie from 1 to max_number+2
# max_number is taken because suppose we have [1,2] then the first missing positive will be 3
# just check sequentially from starting whether any number in this is range is absent then that
# will be our missing first positive
# termination condition is 1 becuase what if we have ony negatives [-1,-2]

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(1, max(nums) + 2):
            found = False
            for j in range(len(nums)):
                if nums[j] <= 0:
                    continue
                if i == nums[j]:
                    found = True
                    break
            if not found:
                return i

        return 1


# Better
# T.C. - O(max_number)
# S.C  - O(max_number)

# Intuition
# Keep track of what element should be present
# increment the number in the map wrt to elements present in original map
# see which numbers count is still zero


from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        should_contain_map = {}
        for i in range(1, max(nums) + 2):
            should_contain_map[i] = 0

        for num in nums:
            if num in should_contain_map:
                should_contain_map[num] += 1

        for num in should_contain_map:
            if should_contain_map[num] == 0:
                return num

        return 1


# Optimal
# T.C. - O(2N) ~ O(N)
# S.C  - O(1)

# Intuition
# Do cyclic cyclic_sort
# ignore number greater than size of array and negative numbers since zero based indexing
# the first number at wro


from typing import List


class Solution:
    def cyclic_sort(self, nums: List[int]) -> None:
        i = 0
        while i < len(nums):
            actualPos = nums[i] - 1
            if nums[i] < len(nums) and nums[i] > 0 and nums[actualPos] != nums[i]:
                nums[i], nums[actualPos] = nums[actualPos], nums[i]
            else:
                i += 1

    def firstMissingPositive(self, nums: List[int]) -> int:
        self.cyclic_sort(nums)

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1

        return -1
