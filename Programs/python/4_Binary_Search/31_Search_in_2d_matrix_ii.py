# https://leetcode.com/problems/search-a-2d-matrix-ii , Medium

# Question
# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.


# Example 1:
# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
# Output: true

# Example 2:
# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
# Output: false


# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= n, m <= 300
# -10^9 <= matrix[i][j] <= 10^9
# All the integers in each row are sorted in ascending order.
# All the integers in each column are sorted in ascending order.
# -10^9 <= target <= 10^9

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
# T.C. - O(N*log(M))
# S.C  - O(1)

# Intuition
# For each row do binary search to
# check if target present


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
            if self.search(matrix[i], target):
                return True
        return False


# Optimal
# T.C. - O(N+M)
# S.C  - O(1)

# Intuition
# Start from either bottom left or top right
# based on the current value check which direction
# to go down or towards left,if far than target
# increase column otherwise decrease row

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ro, co = 0, len(matrix[0]) - 1

        while co >= 0 and ro < len(matrix):
            if matrix[ro][co] == target:
                return True

            if matrix[ro][co] > target:
                co -= 1
            else:
                ro += 1

        return False
