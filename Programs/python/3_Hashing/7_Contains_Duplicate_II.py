# https://leetcode.com/problems/contains-duplicate-ii, Easy, HashMap / Sliding Window

# Question
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

# Example 1:
# Input: nums = [1,2,3,1], k = 3
# Output: true

# Example 2:
# Input: nums = [1,0,1,1], k = 1
# Output: true

# Example 3:
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false

# Constraints:
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 0 <= k <= 10^5

# Brute
# T.C. - O(n^2)
# S.C  - O(1)

# Intuition
# Try finding all the possible pairs which satisfies the condition
# if pair found return true
# return false

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and abs(i - j) <= k:
                    return True

        return False


# Optimal
# T.C. - O(n)
# S.C  - O(n)

# Intuition
# Store all the numbers as you visit them
# if we have already encountered current number before
# we check whether its satisfies the given condition

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        visited = {}

        for idx, num in enumerate(nums):
            if num in visited and abs(idx - visited[num]) <= k:
                return True
            visited[num] = idx

        return False
