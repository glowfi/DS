# https://leetcode.com/problems/4sum , Medium, 2Sum

# Question
# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.


# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Example 2:

# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]


# Constraints:

# 1 <= nums.length <= 200
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9

# Brute
# T.C. - O(N^4)
# S.C  - O(1)

# Intuition
# Generate all possible pairs and check if target sum exists


from contextlib import contextmanager
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = set()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    for l in range(k + 1, len(nums)):
                        sm = nums[i] + nums[j] + nums[k] + nums[l]

                        if sm == target:
                            ans.add((nums[i], nums[j], nums[k], nums[l]))

        return list(ans)


# Better
# T.C. - O(N^3)
# S.C  - O(N)

# Intuition
# Fix one element at index i and other at j and perform 2 sum hashmap technique


from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = set()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                h = {}
                for k in range(j + 1, len(nums)):
                    diff = target - nums[i] - nums[j] - nums[k]
                    if diff in h:
                        ans.add((nums[i], nums[j], nums[k], nums[h[diff]]))
                    h[nums[k]] = k

        return list(ans)


# Optimal
# T.C. - O(N^3)
# S.C  - O(1)

# Intuition
# Fix one element at index i and other at j and perform 2 sum sorted array technique


from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = set()

        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                k, l = j + 1, len(nums) - 1
                while k < l:
                    sm = nums[i] + nums[j] + nums[k] + nums[l]
                    if sm > target:
                        l -= 1
                    elif sm < target:
                        k += 1
                    elif sm == target:
                        ans.add((nums[i], nums[j], nums[k], nums[l]))
                        k += 1
                        l -= 1

                        while nums[k] == nums[k - 1] and k < l:
                            k += 1

                        while nums[l] == nums[l + 1] and k < l:
                            l -= 1

        return list(ans)
