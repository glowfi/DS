# https://leetcode.com/problems/search-insert-position , Easy

# Question
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not,
# return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4


# Constraints:

# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums contains distinct values sorted in ascending order.
# -10^4 <= target <= 10^4


# Optimal
# T.C. - O(log(N))
# S.C  - O(1)

# Intuition
# Find the ceil and return


from typing import List


class Solution:
    def ceil(self, x: int, arr: list[int]):
        st, en = 0, len(arr) - 1
        ans = len(arr)

        while st <= en:
            mid = st + (en - st) // 2

            if arr[mid] >= x:
                ans = mid
                en = mid - 1
            else:
                st = mid + 1

        return ans

    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.ceil(target, nums)
