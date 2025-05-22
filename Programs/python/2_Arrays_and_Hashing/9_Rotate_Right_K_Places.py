# https://leetcode.com/problems/rotate-array , Medium

# Question
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.


# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]


# Constraints:

# 1 <= nums.length <= 10^5
# -2^31 <= nums[i] <= 2^31 - 1
# 0 <= k <= 10^5


# Brute
# T.C. - O(N*k)
# S.C  - O(1)

# Intuition
# keep right rotating by one place for d times


from typing import List


class Solution:
    def right_rotate(self, arr: List[int]):
        for i in range(len(arr) - 1, 0, -1):
            arr[i], arr[i - 1] = arr[i - 1], arr[i]

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k:
            self.right_rotate(nums)
            k -= 1


# Optimal
# T.C. - O(k)+O(N-k)+O(N)
# S.C  - O(1)

# Intuition
# reverse the whole array
# reverse the array from 0 to k-1
# reverse the array from k to len(arr)-1
# perform k normalization

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)

        def rev_array(arr: list[int], i: int, j: int) -> None:

            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        rev_array(nums, 0, len(nums) - 1)
        rev_array(nums, 0, k - 1)
        rev_array(nums, k, len(nums) - 1)
