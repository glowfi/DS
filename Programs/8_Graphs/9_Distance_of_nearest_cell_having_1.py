# https://leetcode.com/problems/01-matrix/ , Medium


# Optimal
# T.C. - O(n^2)+O(n^2)
# S.C  - O(n)

from collections import deque


class Solution:
    def check_in_bounds(self, matrix, ro, co):
        if ro < 0 or co < 0:
            return False
        if ro >= len(matrix) or co >= len(matrix[0]):
            return False
        return True

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque([])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        seen = {}

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    seen[(i, j)] = True
                    q.append([(i, j), 0])

        while q:
            for i in range(len(q)):
                pt, dis = q.popleft()
                x, y = pt

                for dx, dy in dirs:
                    row, col = dx + x, dy + y
                    if self.check_in_bounds(mat, row, col) and (row, col) not in seen:
                        if mat[row][col] == 1:
                            seen[(row, col)] = True
                            mat[row][col] = dis + 1
                            q.append([(row, col), dis + 1])

        return mat
