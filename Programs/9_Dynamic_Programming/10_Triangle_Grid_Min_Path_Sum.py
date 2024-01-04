# https://leetcode.com/problems/triangle/ , Medium


# Recursion
# T.C. - O(N*M)
# S.C  - O(N+M)


class Solution:
    def solve(self, i, j, m, triangle):
        if i >= m:
            return float("inf")

        if i == m - 1:
            return triangle[m - 1][j]

        # Go to ith of next row
        way_1 = self.solve(i + 1, j, m, triangle) + triangle[i][j]

        # Go to (i+1)th of next row
        way_2 = self.solve(i + 1, j + 1, m, triangle) + triangle[i][j]

        return min(way_1, way_2)

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        return self.solve(0, 0, m, triangle)


# Memoization
# T.C. - O(N*M)
# S.C  - O(N+M)+O(N*M)


class Solution:
    def solve(self, i, j, m, triangle, dp):
        if i >= m:
            return float("inf")

        if (i, j) in dp:
            return dp[(i, j)]

        if i == m - 1:
            return triangle[m - 1][j]

        # Go to ith of next row
        way_1 = self.solve(i + 1, j, m, triangle, dp) + triangle[i][j]

        # Go to (i+1)th of next row
        way_2 = self.solve(i + 1, j + 1, m, triangle, dp) + triangle[i][j]

        dp[(i, j)] = min(way_1, way_2)

        return dp[(i, j)]

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        dp = {}
        return self.solve(0, 0, m, triangle, dp)


# Tabulation
# T.C. - O(N*M)
# S.C  - O(N*M)


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)

        dp = [[0 for _ in range(len(triangle[i]))] for i in range(m)]

        for i in range(len(triangle[-1])):
            dp[m - 1][i] = triangle[m - 1][i]

        for i in range(m - 2, -1, -1):
            for j in range(0, len(triangle[i])):
                way_1, way_2 = float("inf"), float("inf")

                if i + 1 < m:
                    way_1 = triangle[i][j] + dp[i + 1][j]
                    way_2 = triangle[i][j] + dp[i + 1][j + 1]

                dp[i][j] = min(way_1, way_2)

        return dp[0][0]


# Space Optimized
# T.C. - O(N*M)
# S.C  - O(col_length_last_row)


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)

        mx_col_length = len(triangle[-1])
        dp = [-1 for _ in range(mx_col_length)]

        for i in range(len(triangle[-1])):
            dp[i] = triangle[m - 1][i]

        for i in range(m - 2, -1, -1):
            tmp = [-1 for _ in range(len(triangle[i]))]
            for j in range(0, len(triangle[i])):
                way_1, way_2 = float("inf"), float("inf")

                if i + 1 < m:
                    way_1 = triangle[i][j] + dp[j]
                    way_2 = triangle[i][j] + dp[j + 1]

                tmp[j] = min(way_1, way_2)
            dp = tmp

        return dp[0]
