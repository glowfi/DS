# https://leetcode.com/problems/squares-of-a-sorted-array, Easy, Two Pointers

# Question
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# Example 2:
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

# Constraints:
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums is sorted in non-decreasing order.

# Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?

# Brute
# T.C. - O(n)+O(nlog(n))
# S.C  - O(n)

# Intuition
# Square each number in the array
# sort the array

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([i * i for i in nums])


# Optimal
# T.C. - O(n)
# S.C  - O(1)

# Intuition
# The array is sorted in non-decreasing order, so negative numbers (if any)
# are on the left and positive numbers are on the right. When we square them,
# both sides become non-negative, and the largest squares will come from the
# values with the largest absolute magnitude, which are at the two ends.
#
# This means the biggest square is always at either the leftmost or rightmost
# position of the current range. So we use two pointers:
# - p1 at the start (left side, large negative numbers)
# - p2 at the end (right side, large positive numbers)
# and a pointer k at the end of the result array.
#
# At each step, we compare nums[p1]^2 and nums[p2]^2:
# - Place the larger square at res[k].
# - Move the corresponding pointer (p1 or p2) inward.
# - Move k one step left to fill the next largest square.

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        k = len(nums) - 1
        p1, p2 = 0, len(nums) - 1
        res = [0] * len(nums)

        while p1 <= p2:
            n1, n2 = nums[p1] ** 2, nums[p2] ** 2

            if n1 > n2:
                res[k] = n1
                p1 += 1
            else:
                res[k] = n2
                p2 -= 1

            k -= 1

        return res
