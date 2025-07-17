# https://leetcode.com/problems/search-in-rotated-sorted-array-ii , Medium

# Question
# There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

# Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

# Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

# You must decrease the overall operation steps as much as possible.


# Example 1:

# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
# Example 2:

# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false


# Constraints:

# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# nums is guaranteed to be rotated at some pivot.
# -10^4 <= target <= 10^4

# Follow up: This problem is similar to Search in Rotated Sorted Array, but nums may contain duplicates. Would this affect the runtime complexity? How and why?


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
                return True

        return False


# Optimal
# T.C. - O(log(N))
# S.C  - O(1)

# Intuition
# Find which part is sorted
# Check if target has possibility to be present in sorted part
# At any point we see that arr[mid],arr[st],arr[en] are equal we move
# start ahead and end pointer backwards and reduce our search space
# as we will not be able to decide which part to go in order to
# reduce search space


from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        st, en = 0, len(nums) - 1

        while st <= en:
            mid = st + (en - st) // 2

            if nums[mid] == target:
                return True

            # Remove duplicates
            if nums[st] == nums[mid] and nums[mid] == nums[en]:
                st += 1
                en -= 1
                continue

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

        return False
