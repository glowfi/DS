# https://leetcode.com/problems/3sum, Medium, TwoPointers after Sorting

# Question
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

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
# T.C. - O(n^3)
# S.C  - O(t)

# Intuition
# Sort the array,since in the question order does not matter
# sorting array will help us eliminate the duplicated when
# we insert it into the set data structure
# Just use 3 loops and pick 3 numbers from each iteration
# and check whether they sum up to zero if yes add them
# to the result

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.add(
                            (
                                nums[i],
                                nums[j],
                                nums[k],
                            )
                        )

        return list(res)


# Better
# T.C. - O(n^2)
# S.C  - O(n)

# Intuition
# Sort the array
# Just use two loops
# basically our task is to check keep
# traversing the array and mark the number
# as visited since we want to find 3 numbers
# that sum up to target zero, we check if
# the diff=0-nums[i]-nums[j] exists in visted
# is present in map or not if that number is
# present we can definitely say we have a triplet

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        for i in range(len(nums)):
            visited = {}
            for j in range(i + 1, len(nums)):
                diff = 0 - nums[i] - nums[j]
                if diff in visited:
                    res.add((nums[i], nums[j], diff))
                visited[nums[j]] = j

        return list(res)


# Optimal
# T.C. - O(n^2)
# S.C  - O(1)

# Intuition
# This is the modified version of Two Sum II
# We avoid duplicates as each step


from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()

        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i - 1]:
                # Avoid duplicates
                continue

            j, k = i + 1, len(nums) - 1

            while j < k:
                sm = nums[i] + nums[j] + nums[k]

                if sm == 0:
                    ans.add(
                        (
                            nums[i],
                            nums[j],
                            nums[k],
                        )
                    )
                    j += 1
                    k -= 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1

                    while nums[k] == nums[k + 1] and j < k:
                        k -= 1

                elif sm > 0:
                    k -= 1

                elif sm < 0:
                    j += 1

        return list(ans)
