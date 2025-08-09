# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array , Medium, BS-In-Rotated-Sorted-Array

# Question
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.


# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
# Example 2:

# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
# Example 3:

# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times.


# Constraints:

# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# All the integers of nums are unique.
# nums is sorted and rotated between 1 and n times.

# Brute
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# Just find the min element in the whole array
# by making a linear scan

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_elem = nums[0]

        for i in range(1, len(nums)):
            min_elem = min(min_elem, nums[i])

        return min_elem


# Optimal
# T.C. - O(log(N))
# S.C  - O(1)

# Intuition
# One key observation is since array is rotated sorted,for
# every index one half will be sorted and other will be unsorted
# we will take the advantage of the sorted property and we are going
# to store the minimum from the sorted in a varaible and discard
# the sorted half and move to the unsorted half as from sorted we
# have already picked up the min element


from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        st, en = 0, len(nums) - 1
        ans = 500

        while st <= en:
            mid = st + (en - st) // 2

            # if we cross the rotated point
            if nums[st] <= nums[mid] and nums[mid] <= nums[en]:
                ans = min(ans, nums[st])
                break

            # if left is sorted
            if nums[st] <= nums[mid]:
                # discard sorted half and move to unsorted
                ans = min(ans, nums[st])
                st = mid + 1

            # right is sorted
            else:
                # discard sorted half and move to unsorted
                ans = min(ans, nums[mid])
                en = mid - 1

        return ans
