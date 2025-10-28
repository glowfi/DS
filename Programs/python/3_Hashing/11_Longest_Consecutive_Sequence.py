# https://leetcode.com/problems/longest-consecutive-sequence, Medium, HashSet / Union-Find

# Question
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.


# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# Example 3:

# Input: nums = [1,0,1,2]
# Output: 3


# Constraints:

# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9

# Brute
# T.C. - O(n^2)
# S.C  - O(1)

# Intuition
# For every value in array check whether its
# consecutive elements are present or not

from typing import List


class Solution:
    def linearSearch(self, arr: List[int], targetVal: int):
        for i in range(len(arr)):
            if arr[i] == targetVal:
                return i
        return -1

    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0

        for i in range(len(nums)):
            curr = nums[i]
            length = 1
            while self.linearSearch(nums, curr + length) != -1:
                length += 1
            longest = max(longest, length)

        return longest


# Better
# T.C. - O(nlog(n))
# S.C  - O(1)

# Intuition
# Sort the array
# Check whether the array follow the consecutive sequence
# pattern

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        longest = 1
        curr_length = 1
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                continue

            if nums[i - 1] == nums[i] - 1:
                curr_length += 1
            else:
                curr_length = 1

            longest = max(longest, curr_length)

        return longest


# Optimal
# T.C. - O(n)+O(2n)
# S.C  - O(n)

# Intuition
# The answer lies in visualization
# consider the below array
# 100 4 200 1 3 2
#
# 1 2 3 4     100        200
# ---------------------------

# convert the given array to set
# starting values of the sequence does not have left neightbour
# so whenever we find an element which does not have left neightbour
# we will start a while loop incrementing it by 1 and check if that
# number exists and keep on building the sequence and atlast we can
# check if its the max length till now or not

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
