# https://leetcode.com/problems/two-sum , Easy

# Question
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]


# Constraints:

# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.

# Brute
# T.C. - O(N^2)
# S.C  - O(1)

# Intuition
# Generate all the pairs and check whether pair exists or not

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# Optimal
# T.C. - O(N)
# S.C  - O(N)

# Intuition
# keep marking the element as you visit them
# just check target-current_element present in seen_map or not
# X+Y=target, if target-Y is present then we can definitely say
# we have a pair

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_map = {}

        for idx, num in enumerate(nums):
            diff = target - num
            if diff in seen_map:
                return [seen_map[diff], idx]
            seen_map[num] = idx
