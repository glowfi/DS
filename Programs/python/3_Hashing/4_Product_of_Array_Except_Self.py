# https://leetcode.com/problems/product-of-array-except-self, Medium, Prefix & Suffix Product / HashMap

# Question
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

# Constraints:
# 2 <= nums.length <= 10^5
# -30 <= nums[i] <= 30
# The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

# Brute
# T.C. - O(n^2)
# S.C  - O(1)

# Intuition
# Use two loop
# Outer loop fixes one element
# Inner loop traverse the entire array and skips the current fixed element
# Also we maintain the product

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)

        for i in range(len(nums)):
            p = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                p *= nums[j]
            res[i] = p

        return res


# Better
# T.C. - O(n)+O(n)+O(n) ~ O(n)
# S.C  - O(n)+O(n) ~ O(n)

# Intuition
# Build a prefix product array
# Build a suffix product array
# for an elemen at pos i its product is nothing but
# multiplication og prefix[i]*suffix[i]

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        pref = [1] * n
        for i in range(1, n):
            pref[i] = pref[i - 1] * nums[i - 1]

        suff = [1] * n
        for i in range(n - 2, -1, -1):
            suff[i] = suff[i + 1] * nums[i + 1]

        ans = [1] * n
        for i in range(n):
            ans[i] = pref[i] * suff[i]

        return ans


# Optimal
# T.C. - O(n)+O(n)
# S.C  - O(1)

# Intuition
# Maintain a prefix and suffix pointers
# Keep updating the prefix in result array from front
# Keep updating the suffix in result array from back

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        pref = 1
        for i in range(len(nums)):
            res[i] = pref
            pref *= nums[i]

        suff = 1
        for j in range(len(nums) - 1, -1, -1):
            res[j] *= suff
            suff *= nums[j]

        return res
