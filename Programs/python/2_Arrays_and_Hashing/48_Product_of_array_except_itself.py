# https://leetcode.com/problems/product-of-array-except-self , Medium, MaintainPrefixSuffix

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
# T.C. - O(N^2)
# S.C  - O(1)

# Intuition
# Find the product of each number except itself
# using 2 loops

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []

        for i in range(n):
            p = 1
            for j in range(n):
                if i == j:
                    continue
                p *= nums[j]
            ans.append(p)

        return ans


# Better
# T.C. - O(N)+O(N)+O(N)
# S.C  - O(N)+O(N)

# Intuition
# Product of array except itself for an ith number is nothing
# but product of prefix sum till i-1 and suffix sum i+1
# Example : [1 2 3 4 5 6]
# Prod of 3 excpe itself is => 1*2 * 4*5*6
#                              --   -----
#                             pref  suff

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
# T.C. - O(N)+O(N)
# S.C  - O(1)

# Intuition
# Fill the result array on the fly
# first put the prefix part in the result
# then put suffix part in the result

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n

        pref = 1
        for i in range(n):
            ans[i] = pref
            pref *= nums[i]

        suff = 1
        for j in range(n - 1, -1, -1):
            ans[j] *= suff
            suff *= nums[j]

        return ans
