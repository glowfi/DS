# https://leetcode.com/problems/single-element-in-a-sorted-array, Medium, XOR

# Question
# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

# Return the single element that appears only once.

# Your solution must run in O(log n) time and O(1) space.


# Example 1:

# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:

# Input: nums = [3,3,7,7,10,11,11]
# Output: 10


# Constraints:

# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^5

# Brute
# T.C. - O(N^2)
# S.C  - O(1)

# Intuition
# just check one by one the count of each element
# in the array if count is equal to return nums


from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            cnt = 0
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    cnt += 1
                if cnt >= 2:
                    break
            if cnt == 1:
                return nums[i]
        return -1


# Better
# T.C. - O(2N) ~ O(N)
# S.C  - O(N)

# Intuition
# maintain a frequency map
# return element with frequency 1


from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        freq_map = {}

        for num in nums:
            freq_map[num] = 1 + freq_map.get(num, 0)

        for num in freq_map:
            if freq_map[num] == 1:
                return num

        return -1


# Optimal
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# we know xor of any 2 same number is 0
# and xor of 0 with any number (x) is x
# so same number get cancelled out leaving
# the element appeating once

from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        xor = 0

        for num in nums:
            xor ^= num

        return xor
