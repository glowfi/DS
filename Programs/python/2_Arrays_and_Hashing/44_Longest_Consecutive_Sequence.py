# https://leetcode.com/problems/longest-consecutive-sequence, Medium, LongestSequence

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
# T.C. - O(Nlog(N)) + O(N)
# S.C  - O(1)

# Intuition
# sort the array and find
# the longest consecutive sequence
# ignore equal length number


from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums.sort()

        mx_len = 1
        curr_len = 1

        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                curr_len += 1
                mx_len = max(mx_len, curr_len)
            elif nums[i] - nums[i - 1] == 0:
                mx_len = max(mx_len, curr_len)
                continue
            else:
                curr_len = 1

        return mx_len


# Optimal
# T.C. - O(N)
# S.C  - O(N)

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
