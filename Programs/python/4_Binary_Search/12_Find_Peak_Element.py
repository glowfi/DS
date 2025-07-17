# https://leetcode.com/problems/find-peak-element , Medium

# Question
# A peak element is an element that is strictly greater than its neighbors.

# Given a 0-indexed integer numsay nums, find a peak element, and return its index. If the numsay contains multiple peaks, return the index to any of the peaks.

# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the numsay.

# You must write an algorithm that runs in O(log n) time.


# Example 1:

# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.
# Example 2:

# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.


# Constraints:

# 1 <= nums.length <= 1000
# -2^31 <= nums[i] <= 2^31 - 1
# nums[i] != nums[i + 1] for all valid i.

# Brute
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# just check which element is greater
# than 2 of its neighbour in single
# pass


from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        for i in range(len(nums)):
            if i == 0 and nums[0] > nums[1]:
                return 0
            elif i == len(nums) - 1 and nums[len(nums) - 1] > nums[len(nums) - 2]:
                return len(nums) - 1

            elif nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return i


# Optimal
# T.C. - O(log(N))
# S.C  - O(1)

# Intuition
# By observation its clear that
# we are at position mid then if we
# that any of the 2 neighbours have
# values higher than current mid
# then we can say that there is a high chance
# we will find the peak there
# walk through an example

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        st, en = 1, len(nums) - 2

        while st <= en:
            mid = st + (en - st) // 2

            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid

            # Find promising canditate in which direction we can find peak

            # if Right Neighbour is promising
            if nums[mid + 1] > nums[mid] and nums[mid + 1] > nums[mid]:
                st = mid + 1

            else:
                # if Left Neighbour is promising
                en = mid - 1

        if len(nums) == 1:
            return 0

        if nums[0] > nums[1]:
            return 0

        if nums[-1] > nums[-2]:
            return len(nums) - 1
