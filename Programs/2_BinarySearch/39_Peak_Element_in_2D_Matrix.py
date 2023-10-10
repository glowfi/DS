# https://leetcode.com/problems/find-a-peak-element-ii/ ,Medium

# Brute
# T.C. -> O(n*m)
# S.C. -> O(1)


class Solution:
    def checkInbounds(self, ro, co, matrix):
        return 0 <= ro < len(matrix) and 0 <= co < len(matrix[0])

    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        ans = []
        ro = len(mat)
        co = len(mat[0])

        for i in range(ro):
            for j in range(co):
                up = (
                    mat[i - 1][j]
                    if self.checkInbounds(i - 1, j, mat)
                    else float("-inf")
                )
                down = (
                    mat[i + 1][j]
                    if self.checkInbounds(i + 1, j, mat)
                    else float("-inf")
                )

                left = (
                    mat[i][j - 1]
                    if self.checkInbounds(i, j - 1, mat)
                    else float("-inf")
                )
                right = (
                    mat[i][j + 1]
                    if self.checkInbounds(i, j + 1, mat)
                    else float("-inf")
                )

                mx = max(up, down, left, right, mat[i][j])

                if mx == mat[i][j]:
                    return [i, j]
        return ans


# Optimal
# T.C. -> O(n*log(m))
# S.C. -> O(1)


class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        l, r = 0, m - 1
        if m == 1:  # one row corner case
            return [0, mat[0].index(max(mat[0]))]

        # binary search for row
        while l <= r:
            mid = (l + r) // 2
            i = mat[mid].index(max(mat[mid]))
            if mid > 0 and mat[mid][i] < mat[mid - 1][i]:
                r = mid - 1
            elif mid < m - 1 and mat[mid][i] < mat[mid + 1][i]:
                l = mid + 1
            else:
                l = mid
                break
        return [l, i]
