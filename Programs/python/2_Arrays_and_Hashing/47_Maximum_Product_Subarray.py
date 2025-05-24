# https://leetcode.com/problems/maximum-sum-circular-subarray , Medium

# Question
# Given an integer array nums, find a subarray that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.


# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


# Constraints:

# 1 <= nums.length <= 2 * 10^4
# -10 <= nums[i] <= 10
# The product of any subarray of nums is guaranteed to fit in a 32-bit integer.

# Brute
# T.C. - O(N^2)
# S.C  - O(1)

# Intuition
# Generate all sub arrays and find the max
# product from it


import sys
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx_prod = -sys.maxsize
        for i in range(len(nums)):
            prod = 1
            for j in range(i, len(nums)):
                prod *= nums[j]
                mx_prod = max(mx_prod, prod)
        return mx_prod


# Optimal
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# Observation 1 : if array has all postive then just return the prod of entire array
# Observation 2: if array has even nos of negative just return the prod of entire array
# Observation 3: if array has odd no of negatives just remove one negative (leaving us with even negative) and the answer will lie in either suffix or prefix
# Observation 4: if we have zero then we will not carry it over as it will reduce our maximum product , we will suffix,prefix to 1,1
# To find the answer, we will check all possible prefix subarrays (starting from index 0) and all possible suffix subarrays (starting from index n-1)
# The maximum product obtained from these prefix and suffix subarrays will be our final answer.

import sys
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pref = 1
        suff = 1
        n = len(nums)
        mx_prod = -sys.maxsize

        for i in range(len(nums)):
            if pref == 0:
                pref = 1
            if suff == 0:
                suff = 1

            pref *= nums[i]
            suff *= nums[n - i - 1]

            mx_prod = max(mx_prod, pref, suff)

        return mx_prod
