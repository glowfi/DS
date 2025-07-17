# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array , Medium

# Question
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.


# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]


# Constraints:

# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# nums is a non-decreasing array.
# -10^9 <= target <= 10^9

# Brute
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# Traverse the array and if you find
# the target number first store it in a
# variable only if we have not see this in past and
# keep traversing forward
# keep track of the last index of the target
# in a variable called last only if we have
# seen in the past


from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first, last = -1, -1
        hasSeenFirst = False

        for idx, num in enumerate(nums):
            if num == target and not hasSeenFirst:
                hasSeenFirst = True
                first = idx
                last = idx

            elif hasSeenFirst and num == target:
                last = idx

        return [first, last]


# Optimal
# T.C. - O(log(N))
# S.C  - O(1)

# Intuition
# For finding first occurence do a bainry search
# keep finding the mid and if we find the number
# then keep going left as we want the first possible occurence
#
# For finding last occurence do a bainry search
# keep finding the mid and if we find the number
# then keep going right as we want the last possible occurence


from typing import List


class Solution:
    def firstOccurence(self, nums: List[int], target: int) -> int:
        ans = -1
        st, en = 0, len(nums) - 1

        while st <= en:
            mid = st + (en - st) // 2

            if nums[mid] == target:
                ans = mid
                en = mid - 1

            elif nums[mid] < target:
                st = mid + 1

            elif nums[mid] > target:
                en = mid - 1

        return ans

    def lastOccurence(self, nums: List[int], target: int) -> int:
        ans = -1
        st, en = 0, len(nums) - 1

        while st <= en:
            mid = st + (en - st) // 2

            if nums[mid] == target:
                ans = mid
                st = mid + 1

            elif nums[mid] < target:
                st = mid + 1

            elif nums[mid] > target:
                en = mid - 1

        return ans

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.firstOccurence(nums, target)
        last = self.lastOccurence(nums, target)

        return [first, last]
