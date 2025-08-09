# https://leetcode.com/problems/sort-an-array , Medium, Basic

# Question
# Given an array of integers nums, sort the array in ascending order and return it.

# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the
# smallest space complexity possible.

# Example 1:

# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions
# of other numbers are changed (for example, 1 and 5).

# Example 2:

# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessairly unique.

# Constraints:

# 1 <= nums.length <= 5 * 10^4
# -5 * 10^4 <= nums[i] <= 5 * 10^4


# Optimal
# T.C. - O(Nlog(N))
# S.C  - O(N)+O(N)

# Intuition
# This algorithms worst,avg,best time complexity is O(Nlog(N)).
# This also use a recursion stack space of O(N) and O(N) auxiliary space to
# store array elements.
# This is a stable sorting algo.
# We follow a divide and conquer strategy we keep divind the
# array into 2 equal halves until they cannot be divided or we are left with array with one element
# and then we keep on merging the two halves until no subarrays are left.

from typing import List


class Solution:
    def merge(self, l: int, mid: int, h: int, arr: list[int]) -> None:
        i, j = l, mid + 1
        tmp = []

        while i <= mid and j <= h:
            if arr[i] <= arr[j]:
                tmp.append(arr[i])
                i += 1
            else:
                tmp.append(arr[j])
                j += 1

        while i <= mid:
            tmp.append(arr[i])
            i += 1
        while j <= h:
            tmp.append(arr[j])
            j += 1

        k = 0
        for i in range(l, h + 1):
            arr[i] = tmp[k]
            k += 1

    def mergeSort(self, l: int, h: int, arr: list[int]) -> None:
        if l >= h:  # array has 1 element
            return

        mid = (l + h) // 2

        self.mergeSort(l, mid, arr)
        self.mergeSort(mid + 1, h, arr)
        self.merge(l, mid, h, arr)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(0, len(nums) - 1, nums)
        return nums
