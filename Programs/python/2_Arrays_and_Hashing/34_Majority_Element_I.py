# https://leetcode.com/problems/majority-element , Easy

# Question
# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the
# majority element always exists in the array.


# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2


# Constraints:

# n == nums.length
# 1 <= n <= 5 * 10^4
# -10^9 <= nums[i] <= 10^9

# Brute
# T.C. - O(N^2)
# S.C  - O(1)

# Intuition
# Keep track of the element appearing more
# than n//2 times using 2 loops


from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_element = -1
        appear_count = len(nums) // 2

        for i in range(len(nums)):
            c = 1
            for j in range(len(nums)):
                if j == i:
                    continue

                if nums[i] == nums[j]:
                    c += 1

            if c > appear_count:
                majority_element = nums[i]

        return majority_element


# Better
# T.C. - O(N)
# S.C  - O(N)

# Intuition
# store the frequency of each element
# and just keep checking if some element
# occur more than n//2 times

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        appear_count = len(nums) // 2
        freq_mp = {}

        for num in nums:
            if num not in freq_mp:
                freq_mp[num] = 1
            else:
                freq_mp[num] += 1

            if freq_mp[num] > appear_count:
                return num

        return -1


# Optimal
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# Observation - we can have atmost k-1 majority elements for n//k
# For example:
# for n=4 if n//2 given we can have only 1 majority element
# than can occur 3 times and 1 element can occur 1 time
# [1,1,1,2] for n//2
# for n=10 if n//3 given we can have only 2 majority elements
# than can occur 4 times each and 2 element can occur 1 time
# [1,1,1,1,2,2,2,2,3,3] for n//3
# 2 pass algo one to find and one to verify
# basically this algos main Intuition is element occuring more than n//2
# times will cancel out the elements occuring less number of times
# + assume first element as majority element
# + if you see majority element again increment count
# + if you see new element decrement count
# + if count is zero new majority element has come


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = nums[0]
        c = 1

        for i in range(1, len(nums)):
            # increment count if its the same majority element
            if nums[i] == maj:
                c += 1

            elif c == 0:  # reset majority element
                c = 1
                maj = nums[i]

            # decrement count if its not the current majority element
            elif nums[i] != maj:
                c -= 1

        return maj
