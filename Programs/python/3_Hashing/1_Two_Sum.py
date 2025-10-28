# https://leetcode.com/problems/two-sum, Easy, HashMap / Complement Lookup

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


# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

# Brute
# T.C. - O(n^2)
# S.C  - O(1)

# Intuition
# Check all possible pairs and find out
# the pair that gives us the given target

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# Optimal
# T.C. - O(n)
# S.C  - O(1)

# Intuition
# We know that if x+y = target
# if are going to do a complement look up
# we are going to mark all the visited elements using a map
# and Check if we have encounter target-y earlier or not


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in visited:
                return [i, visited[diff]]

            visited[nums[i]] = i
