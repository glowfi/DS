# https://leetcode.com/problems/search-in-rotated-sorted-array, Medium, BS-In-Rotated-Sorted-Array

# Question
# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.


# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:

# Input: nums = [1], target = 0
# Output: -1


# Constraints:

# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -10^4 <= target <= 10^4


# Brute
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# Do a linear search to find the target

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i

        return -1


# Optimal
# T.C. - O(log(N))
# S.C  - O(1)

# Intuition
# Find which part is sorted
# Check if target has possibility to be present in sorted part

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        st, en = 0, len(nums) - 1

        while st <= en:
            mid = st + (en - st) // 2

            if nums[mid] == target:
                return mid

            # Check which part is sorted

            # if right is sorted
            if nums[mid] <= nums[en]:
                # target is definitely present in right
                if nums[mid] <= target <= nums[en]:
                    st = mid + 1
                else:
                    en = mid - 1
            # if left is sorted
            else:
                # target is definitely present in left
                if nums[st] <= target <= nums[mid]:
                    en = mid - 1
                else:
                    st = mid + 1

        return -1
