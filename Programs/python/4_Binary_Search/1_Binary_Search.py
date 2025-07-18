# https://leetcode.com/problems/binary-search , Easy

# Question
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums.
# If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.


# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1


# Constraints:

# 1 <= nums.length <= 10^4
# -10^4 < nums[i], target < 10^4
# All the integers in nums are unique.
# nums is sorted in ascending order.

# Optimal
# T.C. - O(log(N))
# S.C  - O(1)

# Intuition
# Every time find the mid index
# if the element at the mid index is lesser than target ,
# then move the start pointer to mid+1 as all the elements in
# the left of mid will always be smaller no need to go in that direction
# if the element at the mid index is greater than target ,
# then move the end pointer to mid-1 as all the elements in
# the right of mid will always be greater no need to go in that direction


from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        st, en = 0, len(nums) - 1

        while st <= en:
            mid = st + (en - st) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                st = mid + 1

            elif nums[mid] > target:
                en = mid - 1

        return -1
