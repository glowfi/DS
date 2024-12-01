# https://leetcode.com/problems/spiral-matrix/description/,Medium

# Brute
# T.C. -> O(n*m)
# S.C. -> O(n*m)


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        left = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1

        ans = []

        while left <= right and top <= bottom:
            # Left to Right
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1

            # Top to Bottom
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1

            # Right to Left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1

            # Bottom to Top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1

        return ans
