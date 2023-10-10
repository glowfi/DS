# https://leetcode.com/problems/search-a-2d-matrix/ , Medium


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
# T.C. -> O(m)+O(log(n))
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
                if matrix[i][0] <= target and target <= matrix[i][-1]:
                    return self.search(matrix[i], target)
        return False


# Optimal
# T.C. -> O(log(m*n))
# S.C. -> O(1)


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        st, en = 0, (m * n) - 1

        while st <= en:
            mid = st + (en - st) // 2

            ro = mid // n
            co = mid % n

            if matrix[ro][co] == target:
                return True

            elif matrix[ro][co] < target:
                st = mid + 1

            else:
                en = mid - 1

        return False
