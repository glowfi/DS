# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold , Medium

# Question
# Given an array of integers nums and an integer threshold, we will choose a positive integer divisor, divide all the array by it, and sum the division's result. Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

# Each result of the division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

# The test cases are generated so that there will be an answer.


# Example 1:

# Input: nums = [1,2,5,9], threshold = 6
# Output: 5
# Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1.
# If the divisor is 4 we can get a sum of 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2).
# Example 2:

# Input: nums = [44,22,33,11,1], threshold = 5
# Output: 44


# Constraints:

# 1 <= nums.length <= 5 * 10^4
# 1 <= nums[i] <= 10^6
# nums.length <= threshold <= 10^6

# Brute
# T.C. - O(max(nums)*N)+O(N)
# S.C  - O(1)

# Intuition
# we start a linear serch with start index
# as 1 and end index as max number in nums
# first time we encounter a number which
# is able to sum up within the given threshold
# we return the number

import math
from typing import List


class Solution:
    def sumWithinThreshold(self, nums: List[int], threshold: int, divisor: int):
        s = 0

        for num in nums:
            s += math.ceil(num / divisor)

        return s <= threshold

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        for i in range(1, max(nums) + 1):
            if self.sumWithinThreshold(nums, threshold, i):
                return i
        return -1


# Optimal
# T.C. - O(log(max(nums))*N)+O(N)
# S.C  - O(1)

# Intuition
# we start a binary search with start index
# and end index as 1 and max number among the
# the given array,if we are able to find the
# sum that divides all number within threshold
# we go left to minimize the number otherwise
# we go to right

import math
from typing import List


class Solution:
    def sumWithinThreshold(self, nums: List[int], threshold: int, divisor: int):
        s = 0

        for num in nums:
            s += math.ceil(num / divisor)

        return s <= threshold

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        st, en = 1, max(nums) + 1
        ans = -1

        while st <= en:
            mid = st + (en - st) // 2

            if self.sumWithinThreshold(nums, threshold, mid):
                en = mid - 1
                ans = mid
            else:
                st = mid + 1

        return ans
