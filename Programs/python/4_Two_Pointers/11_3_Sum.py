# https://leetcode.com/problems/3sum, Medium, TwoPointers after Sorting

# Question
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such
# that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
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
# We first sort the array. Sorting helps in two ways: it makes the numbers easier to work with,
# and it ensures that any triplet we pick will be in a fixed, sorted order, which is useful for removing duplicates.
# After sorting, we use three nested loops to try every possible combination of three
# different indices i, j, and k (with i < j < k). For each combination, we check whether
# nums[i] + nums[j] + nums[k] equals zero. If it does, then we have found a valid triplet.

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

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
# The key idea is to fix one number and then reduce the problem to a “two-sum” style search for the other two numbers.
# After sorting, pick one number as the first element of the triplet.
# Now the problem becomes: can we find two other numbers in the remaining part
# of the array whose sum is equal to the value that balances this first number to
# reach zero? To do that efficiently, we use a hash-based check: as we scan through the
# remaining numbers, we keep track of which values we’ve already seen, and for each
# new value we ask, “Is there another value we saw earlier that would complete the triplet to sum to zero?”
# Whenever that condition is met, we’ve found a valid triplet. Sorting ensures that each
# triplet has a consistent order, which makes it easy to avoid counting the same combination more than once.

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for i in range(len(nums)):
            mp = {}
            for j in range(i + 1, len(nums)):
                complement = 0 - nums[i] - nums[j]
                if complement in mp:
                    res.add(
                        (
                            nums[i],
                            nums[j],
                            complement,
                        )
                    )
                mp[nums[j]] = j

        return list(res)


# Optimal
# T.C. - O(n^2)
# S.C  - O(1)

# Intuition
# This is a modified version of the Two Sum II pattern extended to three numbers.
#
# 1) Sort the array.
#    Once sorted, we can fix one number nums[i] and then search for two numbers
#    nums[j] and nums[k] such that nums[i] + nums[j] + nums[k] == 0 using
#    a standard two-pointer approach on the subarray to the right of i.
#
# 2) Two-pointer search for each fixed i.
#    For each index i:
#      - Set j = i + 1 (start of the remaining subarray)
#      - Set k = len(nums) - 1 (end of the array)
#    Then:
#      - If the sum is too small, move j right to increase the sum.
#      - If the sum is too large, move k left to decrease the sum.
#      - If the sum is exactly zero, we record this triplet.
#
# 3) Avoiding duplicates for i, j, and k.
#    Because the array can contain duplicates, we must be careful not to produce
#    the same triplet multiple times.


from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums)):
            # skip duplicate
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, len(nums) - 1

            while j < k:
                sm = nums[i] + nums[j] + nums[k]

                if sm == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    # skip duplicates from left
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    # skip duplicates from right
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

                elif sm > 0:
                    k -= 1

                else:
                    j += 1

        return ans
