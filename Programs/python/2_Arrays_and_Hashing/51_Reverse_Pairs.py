# https://leetcode.com/problems/reverse-pairs , Hard, MergeSort

# Question
# Given an integer array nums, return the number of reverse pairs in the array.

# A reverse pair is a pair (i, j) where:

# 0 <= i < j < nums.length and
# nums[i] > 2 * nums[j].


# Example 1:

# Input: nums = [1,3,2,3,1]
# Output: 2
# Explanation: The reverse pairs are:
# (1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
# (3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1
# Example 2:

# Input: nums = [2,4,3,5,1]
# Output: 3
# Explanation: The reverse pairs are:
# (1, 4) --> nums[1] = 4, nums[4] = 1, 4 > 2 * 1
# (2, 4) --> nums[2] = 3, nums[4] = 1, 3 > 2 * 1
# (3, 4) --> nums[3] = 5, nums[4] = 1, 5 > 2 * 1


# Constraints:

# 1 <= nums.length <= 5 * 10^4
# -2^31 <= nums[i] <= 2^31 - 1

# Brute
# T.C. - O(N^2)
# S.C  - O(1)

# Intuition
# generate all pairs and check
# which pairs follow the condition


from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        c = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j] * 2:
                    c += 1
        return c


# Optimal
# T.C. - O(NlogN)
# S.C  - O(N)

# Intuition
# use merge sort to solve this
# Suppose we have 2 sorted array as below
# [5,6,7,8] [1,2,3,4]
# one thing for sure is (5,1)(5,2)
# will form pair right as i<j and arr[i]>2*arr[j]
# but in merge sort after we have proceessed a smaller
# number we move one position ahead but this may lead
# to missing of many pair, so since 2 arrays are sorted
# we can for sure say if 5 forms pair then all the further
# elements will form pair too and add those pair to counter


class Solution:
    def merge(self, l: int, mid: int, h: int, arr: list[int]) -> int:
        c = 0
        i, j = l, mid + 1
        while i <= mid and j <= h:  #  check the condition before performing merge sort
            if arr[i] > 2 * arr[j]:
                c += (mid - i) + 1
                j += 1
            else:
                i += 1

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

        return c

    def mergeSort(self, l: int, h: int, arr: list[int]) -> int:
        c = 0

        if l >= h:  # array has 1 element
            return 0

        mid = (l + h) // 2

        c += self.mergeSort(l, mid, arr)
        c += self.mergeSort(mid + 1, h, arr)
        c += self.merge(l, mid, h, arr)

        return c

    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(0, len(nums) - 1, nums)
