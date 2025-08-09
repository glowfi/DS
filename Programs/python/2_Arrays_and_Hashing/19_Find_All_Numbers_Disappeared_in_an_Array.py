# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array , Easy, CyclicSort

# Question
# Given an array nums of n integers where nums[i] is in the range [1, n], return an
# array of all the integers in the range [1, n] that do not appear in nums.


# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:

# Input: nums = [1,1]
# Output: [2]


# Constraints:

# n == nums.length
# 1 <= n <= 10^5
# 1 <= nums[i] <= n


# Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

# Brute
# T.C. - O(3N) ~ O(N)
# S.C  - O(2N)

# Intuition
# create a map containing items that should be present
# create a map containing current items in array
# iterate through the should_contain_map and check which
# elements are not in curr_contain_map


from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        should_contain_map = {i: True for i in range(1, len(nums) + 1)}
        curr_contain_map = {i: True for i in nums}

        ans = []
        for k, v in should_contain_map.items():
            if k not in curr_contain_map:
                ans.append(k)

        return ans


# Optimal
# T.C. - O(2N) ~ O(N)
# S.C  - O(1)

# Intuition
# Do cyclic sort
# after cyclic sort does the element expected for that index match

from typing import List


class Solution:
    def cyclic_sort(self, arr: List[int]) -> None:
        idx = 0

        while idx < len(arr):
            actualPos = arr[idx] - 1

            if arr[actualPos] != arr[idx]:
                arr[actualPos], arr[idx] = arr[idx], arr[actualPos]
            else:
                idx += 1

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        self.cyclic_sort(nums)

        ans = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                ans.append(i + 1)

        return ans
