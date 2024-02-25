# https://www.geeksforgeeks.org/problems/shortest-common-supersequence0322/1 , Medium


# Recursion
# T.C. - O(ind1*ind2*2^n)
# S.C  - O(min(ind1,ind2))


class Solution:
    def solve(self, i1, i2, X, Y):
        if i1 == 0 or i2 == 0:
            return 0

        match, notMatch = 0, 0

        if X[i1 - 1] == Y[i2 - 1]:
            match = 1 + self.solve(i1 - 1, i2 - 1, X, Y)

        else:
            notMatch = max(self.solve(i1 - 1, i2, X, Y), self.solve(i1, i2 - 1, X, Y))

        return max(match, notMatch)

    def shortestCommonSupersequence(self, X, Y, m, n):
        lcs_length = self.solve(m, n, X, Y)

        return (m + n) - lcs_length


# Memoization
# T.C. - O(ind1*ind2*n)
# S.C  - O(min(ind1,ind2))+O(ind1*ind2)


class Solution:
    def solve(self, i1, i2, X, Y, dp):
        if (i1, i2) in dp:
            return dp[(i1, i2)]

        if i1 == 0 or i2 == 0:
            return 0

        match, notMatch = 0, 0

        if X[i1 - 1] == Y[i2 - 1]:
            match = 1 + self.solve(i1 - 1, i2 - 1, X, Y, dp)

        else:
            notMatch = max(
                self.solve(i1 - 1, i2, X, Y, dp), self.solve(i1, i2 - 1, X, Y, dp)
            )

        dp[(i1, i2)] = max(match, notMatch)

        return dp[(i1, i2)]

    def shortestCommonSupersequence(self, X, Y, m, n):
        lcs_length = self.solve(m, n, X, Y, {})

        return (m + n) - lcs_length


# Tabulation
# T.C. - O(ind1*ind2)
# S.C  - O(ind1*ind2)


class Solution:
    def shortestCommonSupersequence(self, X, Y, m, n):
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i1 in range(m + 1):
            for i2 in range(n + 1):
                if i1 == 0 or i2 == 0:
                    dp[i1][i2] = 0
                else:
                    match, notMatch = 0, 0

                    if X[i1 - 1] == Y[i2 - 1]:
                        match = 1 + dp[i1 - 1][i2 - 1]
                    else:
                        notMatch = max(dp[i1 - 1][i2], dp[i1][i2 - 1])

                    dp[i1][i2] = max(match, notMatch)

        lcs_length = dp[m][n]

        return (m + n) - lcs_length


# Space Optimized
# T.C. - O(ind1*ind2)
# S.C  - O(ind2)


class Solution:
    def shortestCommonSupersequence(self, X, Y, m, n):
        dp = [0 for _ in range(n + 1)]

        for i1 in range(m + 1):
            tmp = [0 for _ in range(n + 1)]
            for i2 in range(n + 1):
                if i1 == 0 or i2 == 0:
                    tmp[i2] = 0
                else:
                    match, notMatch = 0, 0

                    if X[i1 - 1] == Y[i2 - 1]:
                        match = 1 + dp[i2 - 1]
                    else:
                        notMatch = max(dp[i2], tmp[i2 - 1])

                    tmp[i2] = max(match, notMatch)
            dp = tmp

        lcs_length = dp[n]

        return (m + n) - lcs_length
