# https://leetcode.com/problems/row-with-maximum-ones, Easy, Bs-on-2d-matrix

# Question
# Given a m x n binary matrix mat, find the 0-indexed position of the row that contains the maximum count of ones, and the number of ones in that row.

# In case there are multiple rows that have the maximum count of ones, the row with the smallest row number should be selected.

# Return an array containing the index of the row, and the number of ones in it.


# Example 1:

# Input: mat = [[0,1],[1,0]]
# Output: [0,1]
# Explanation: Both rows have the same number of 1's. So we return the index of the smaller row, 0, and the maximum count of ones (1). So, the answer is [0,1].
# Example 2:

# Input: mat = [[0,0,0],[0,1,1]]
# Output: [1,2]
# Explanation: The row indexed 1 has the maximum count of ones (2). So we return its index, 1, and the count. So, the answer is [1,2].
# Example 3:

# Input: mat = [[0,0],[1,1],[0,0]]
# Output: [1,2]
# Explanation: The row indexed 1 has the maximum count of ones (2). So the answer is [1,2].


# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 100
# mat[i][j] is either 0 or 1.

# Brute
# T.C. - O(N*M)
# S.C  - O(1)

# Intuition
# Traverse the entire matrix and find the row
# with max ones , keeping track of max count
# of 1 till now for each row


from typing import List


class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        curr_max_row_index = 0
        curr_max_row_count = 0

        for i in range(len(mat)):
            c = 0
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    c += 1
            if c > curr_max_row_count:
                curr_max_row_index = i
                curr_max_row_count = c

        return [curr_max_row_index, curr_max_row_count]


# Optimal
# T.C. - O(N*log(m))
# S.C  - O(1)

# Intuition
# for each row find the last and first occurence
# of 1 and get the count of 1 in each row by doing
# sustraction of lastOccurence and firstOccurence
# and add 1, keep track of max ones in each row
# and max count


from typing import List


class Solution:
    def firstOccurence(self, nums: List[int], target: int) -> int:
        ans = -1
        st, en = 0, len(nums) - 1

        while st <= en:
            mid = st + (en - st) // 2

            if nums[mid] == target:
                ans = mid
                en = mid - 1

            elif nums[mid] < target:
                st = mid + 1

            elif nums[mid] > target:
                en = mid - 1

        return ans

    def lastOccurence(self, nums: List[int], target: int) -> int:
        ans = -1
        st, en = 0, len(nums) - 1

        while st <= en:
            mid = st + (en - st) // 2

            if nums[mid] == target:
                ans = mid
                st = mid + 1

            elif nums[mid] < target:
                st = mid + 1

            elif nums[mid] > target:
                en = mid - 1

        return ans

    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        curr_max_row_index = 0
        curr_max_row_count = 0

        for i in range(len(mat)):
            first_occurence = self.firstOccurence(sorted(mat[i]), 1)
            if first_occurence != -1:
                last_occurence = self.lastOccurence(sorted(mat[i]), 1)
                one_count = last_occurence - first_occurence + 1
                if one_count > curr_max_row_count:
                    curr_max_row_index = i
                    curr_max_row_count = one_count

        return [curr_max_row_index, curr_max_row_count]
