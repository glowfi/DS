# https://leetcode.com/problems/median-of-two-sorted-arrays , Hard

# Question
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

# Constraints:

# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10^6 <= nums1[i], nums2[i] <= 10^6

# Brute
# T.C. - O(Nlog(M))
# S.C  - O(N)

# Intuition
# Merge into a temporary array
# sort the temporary array
# find the median

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        tmp = sorted([*nums1, *nums2])

        mid = len(tmp) // 2
        if len(tmp) % 2 == 1:
            return tmp[mid]
        return (tmp[mid] + tmp[mid - 1]) / 2


# Better
# T.C. - O(N)+O(M)
# S.C  - O(1)

# Intuition
# Use the merge sort algo to find the indexes
# as in merge sort algo we process the array
# in sorted order,pre calcuate uptill which
# index to process for even keep track of last
# and seclast and for odd keep track of last only

from typing import List


class Solution:
    def merge2SortedArray(
        self, arr1: list[int], arr2: list[int], target: int
    ) -> tuple[int, int]:
        i, j = 0, 0
        c = 0
        last = -1
        secLast = -1

        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                secLast = last
                last = arr1[i]
                i += 1
                c += 1
            else:
                secLast = last
                last = arr2[j]
                j += 1
                c += 1

            if c == target:
                return last, secLast

        while i < len(arr1):
            secLast = last
            last = arr1[i]
            i += 1
            c += 1

            if c == target:
                return last, secLast

        while j < len(arr2):
            secLast = last
            last = arr2[j]
            j += 1
            c += 1

            if c == target:
                return last, secLast

        return last, secLast

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mid = (len(nums1) + len(nums2)) // 2
        n = len(nums1) + len(nums2)
        last, secLast = self.merge2SortedArray(nums1, nums2, mid + 1)

        if n % 2 == 0:
            return (last + secLast) / 2
        return last


# Optimal
# T.C. -
# S.C  -

# Intuition
