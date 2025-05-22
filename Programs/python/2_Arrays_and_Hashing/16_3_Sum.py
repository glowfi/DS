# https://leetcode.com/problems/3sum , Medium

# Question
# Given an integer array nums, return all the
# triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.


# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.


# Constraints:

# 3 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5

# Brute
# T.C. - O(N^3)+O(Nlog(N))
# S.C  - O(1)

# Intuition
# Sort the array to generate distinct pairs
# generate all possible triplet combination and see
# whether they add to 0


from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        ans.add((nums[i], nums[j], nums[k]))

        return list(ans)


# Better
# T.C. - O(N^2)+O(Nlog(N))
# S.C  - O(N)

# Intuition
# Fix one element at index i and perform 2 sum hashmap technique

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()

        for i in range(len(nums)):
            h = {}
            for j in range(i + 1, len(nums)):
                diff = 0 - nums[i] - nums[j]
                if diff in h:
                    ans.add((nums[i], nums[j], nums[h[diff]]))
                h[nums[j]] = j

        return list(ans)


# Optimal
# T.C. - O(N^2)+O(Nlog(N))
# S.C  - O(1)

# Intuition
# Fix one element at index i and perform 2 sum sorted array technique

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()

        for i in range(len(nums)):
            j, k = i + 1, len(nums) - 1

            if (
                i != 0 and nums[i] == nums[i - 1]
            ):  # we dont want to generate same triplets
                continue

            while j < k:
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] == 0:
                    ans.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1

                    # we dont want to generate same triplets
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                    while nums[k] == nums[k + 1] and j < k:
                        k -= 1

        return list(ans)
