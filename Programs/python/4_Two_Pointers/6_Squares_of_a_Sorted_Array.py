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
# Since the array is sorted in non-decreasing order we know
# that the left side contains biggest negative numbers and
# right side contains biggest positive numbers. So when we
# are going to square the numbers every number is going to
# become positive.so out biggest square lies on the two
# ends of the array.So we can start with the two ends of the
# array and then move in for smaller numbers.We use a two pointer
# technique to do this.We take 2 pointer p1 and p2 and check which
# value is greater and place the greater values at the end of the array
# A k pointer is also taken to store the postion to store the squared
# value

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        p1, p2 = 0, len(nums) - 1
        k = len(nums) - 1

        while p1 <= p2:
            if abs(nums[p1]) > abs(nums[p2]):
                res[k] = nums[p1] ** 2
                k -= 1
                p1 += 1
            else:
                res[k] = nums[p2] ** 2
                k -= 1
                p2 -= 1

        return res
