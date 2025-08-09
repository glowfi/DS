# https://leetcode.com/problems/search-a-2d-matrix , Medium, Bs-on-2d-matrix

# Question
# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.
# Example 1:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

# Example 2:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false


# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -10^4 <= matrix[i][j], target <= 10^4

# Brute
# T.C. - O(N*M)
# S.C  - O(1)

# Intuition
# Just do a linear search and
# check if target present


from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    return True
        return False


# Better
# T.C. - O(N)+O(log(M))
# S.C  - O(1)

# Intuition
# Traverse throgh each row and if a target
# falls into the row range start a binary
# search


from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        st, en = 0, len(nums) - 1

        while st <= en:
            mid = st + (en - st) // 2

            if nums[mid] == target:
                return True

            elif nums[mid] < target:
                st = mid + 1

            elif nums[mid] > target:
                en = mid - 1

        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][0] == target or matrix[i][-1] == target:
                return True

            if matrix[i][0] < target < matrix[i][-1]:
                if self.search(matrix[i], target):
                    return True

        return False


# Optimal
# T.C. - O(log(N*M))
# S.C  - O(1)

# Intuition
# Just image you have a flattened 1D array
# do a binary search
# for converting 1d co-ordinate to 2d Just
# use the below
# For row -> mid // n
# For col -> mid % n

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        st, en = 0, (rows * cols) - 1

        while st <= en:
            mid = st + (en - st) // 2
            ro = mid // cols
            co = mid % cols

            if matrix[ro][co] == target:
                return True

            if matrix[ro][co] > target:
                en = mid - 1

            else:
                st = mid + 1

        return False
