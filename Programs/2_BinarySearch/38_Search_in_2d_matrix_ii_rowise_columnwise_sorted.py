# https://leetcode.com/problems/search-a-2d-matrix-ii/ , Medium


# Brute
# T.C. -> O(n*m)
# S.C. -> O(1)


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    return True
        return False


# Better
# T.C. -> O(m*log(n))
# S.C. -> O(1)


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        st, en = 0, len(nums) - 1

        while st <= en:
            mid = (st) + (en - st) // 2

            if nums[mid] == target:
                return True

            elif nums[mid] < target:
                st = mid + 1

            elif nums[mid] > target:
                en = mid - 1

        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if self.search(matrix[i], target):
                    return True
        return False


# Optimal
# T.C. -> O(n+m)
# S.C. -> O(1)


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ro, co = 0, len(matrix[0]) - 1

        while co >= 0 and ro < len(matrix):
            if matrix[ro][co] == target:
                return True

            elif target > matrix[ro][co]:
                ro += 1

            else:
                co -= 1

        return False
