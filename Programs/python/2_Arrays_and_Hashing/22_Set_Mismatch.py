# https://leetcode.com/problems/set-mismatch, Easy, CyclicSort

# Question
# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error,
# one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

# You are given an integer array nums representing the data status of this set after the error.

# Find the number that occurs twice and the number that is missing and return them in the form of an array.


# Example 1:

# Input: nums = [1,2,2,4]
# Output: [2,3]
# Example 2:

# Input: nums = [1,1]
# Output: [1,2]


# Constraints:

# 2 <= nums.length <= 10^4
# 1 <= nums[i] <= 10^4

# Brute
# T.C. - O(4N) ~ O(N)
# S.C  - O(1)

# Intuition
# For missing number keep track of what should be present
# and compare it with current present map
# For duplicate find the number with frequency more than 2


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = []

        should_contain_map = {i: True for i in range(1, len(nums) + 1)}

        current_contain_map = {}
        for num in nums:
            current_contain_map[num] = 1 + current_contain_map.get(num, 0)

        for num in current_contain_map:
            if current_contain_map[num] > 1:
                ans.append(num)

        for num in should_contain_map:
            if num not in current_contain_map:
                ans.append(num)

        return ans


# Optimal
# T.C. - O(2N) ~ O(N)
# S.C  - O(1)


# Intuition
# do cyclic sort
# numbers not at correct place is the duplicate and index is the missing

from typing import List


class Solution:
    def cyclic_sort(self, nums: List[int]) -> None:
        i = 0
        while i < len(nums):
            actualPos = nums[i] - 1
            if nums[actualPos] != nums[i]:
                nums[i], nums[actualPos] = nums[actualPos], nums[i]
            else:
                i += 1

    def findErrorNums(self, nums: List[int]) -> List[int]:
        self.cyclic_sort(nums)

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return [nums[i], i + 1]

        return []
