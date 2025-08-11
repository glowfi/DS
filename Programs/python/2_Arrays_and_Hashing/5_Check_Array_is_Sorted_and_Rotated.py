# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated, Easy, Rotation

# Question
# Given an array nums, return true if the array was originally sorted in non-decreasing order,
# then rotated some number of positions (including zero). Otherwise, return false.

# There may be duplicates in the original array.

# Note: An array A rotated by x positions results in an array B of the same length such that B[i] == A[(i+x) % A.length] for every valid index i.


# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: true
# Explanation: [1,2,3,4,5] is the original sorted array.
# You can rotate the array by x = 3 positions to begin on the element of value 3: [3,4,5,1,2].
# Example 2:

# Input: nums = [2,1,3,4]
# Output: false
# Explanation: There is no sorted array once rotated that can make nums.
# Example 3:

# Input: nums = [1,2,3]
# Output: true
# Explanation: [1,2,3] is the original sorted array.
# You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.

# Constraints:

# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100

# Brute
# T.C. - O(N^2)
# S.C  - O(1)

# Intuition
# keep rotating the array by one n times
# then check if the current rotated array is sorted or not
# if in at any pass we see that the array becomes equal to its sorted state
# we return true otherwise we return false

from typing import List


class Solution:
    def rotateByOne(self, nums: list[int]):
        for i in range(len(nums) - 1):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]

    def check_array_sorted(self, nums: list[int]) -> bool:
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                return False
        return True

    def check(self, nums: List[int]) -> bool:
        for _ in range(len(nums)):
            self.rotateByOne(nums)
            if self.check_array_sorted(nums):
                return True
        return False


# Optimal1
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# Suppose ->  [3 4 5 1 2]
#              ----- ---
#               R1    R2
# Check for valid increasing order in region I
# Check for valid increasing order in region II
# and also all elements in region II should be lesser than
# equal to first element in region I
# Think for [1,3,2] also for return case

from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        break_point = -1
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                break_point = i
                break

        if break_point == -1:
            return True

        first_element = nums[0]
        for j in range(break_point + 1, len(nums)):
            if nums[j] > first_element:
                return False
            if nums[j] < nums[j - 1]:
                return False

        return True if nums[-1] <= nums[0] else False


# Optimal
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# Suppose ->  [3 4 5 1 2]
# Number of dips should be 0 or 1
# if more than 1 return False
# Think for [1,3,2] also for return case

from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        dips = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                dips += 1

            if dips > 1:
                return False

        if dips == 0:
            return True

        return nums[-1] <= nums[0] and dips == 1
