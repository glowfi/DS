# https://leetcode.com/problems/distinct-subsequences/ , Hard


# Recursion
# T.C. - O(2^(n*m))
# S.C  - O(n+m)


class Solution:
    def solve(self, i: int, j: int, s: str, t: str) -> int:
        # Base Case
        if j == 0:
            return 1

        if i == 0:
            return 0

        # Try out all ways
        match, notMatch = 0, 0

        # Match
        if s[i - 1] == t[j - 1]:
            match = self.solve(i - 1, j - 1, s, t) + self.solve(i - 1, j, s, t)
            return match

        else:
            # notMatch
            notMatch = self.solve(i - 1, j, s, t)
            return notMatch

    def numDistinct(self, s: str, t: str) -> int:
        return self.solve(len(s), len(t), s, t)


# Memoization
# T.C. - O(N*M)
# S.C  - O(n+m)+O(n*m)


class Solution:
    def solve(self, i: int, j: int, s: str, t: str, dp: dict) -> int:
        if (i, j) in dp:
            return dp[(i, j)]

        # Base Case
        if j == 0:
            return 1

        if i == 0:
            return 0

        # Try out all ways
        match, notMatch = 0, 0

        # Match
        if s[i - 1] == t[j - 1]:
            match = self.solve(i - 1, j - 1, s, t, dp) + self.solve(i - 1, j, s, t, dp)
            dp[(i, j)] = match
            return dp[(i, j)]

        else:
            # notMatch
            notMatch = self.solve(i - 1, j, s, t, dp)
            dp[(i, j)] = notMatch
            return dp[(i, j)]

    def numDistinct(self, s: str, t: str) -> int:
        return self.solve(len(s), len(t), s, t, {})


# Tabulation
# T.C. - O(N*M)
# S.C  - O(n*m)


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]

        for i in range(len(s) + 1):
            for j in range(len(t) + 1):
                if j == 0:
                    dp[i][j] = 1
                elif i == 0:
                    dp[i][j] = 0
                else:
                    if s[i - 1] == t[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i - 1][j]

        return dp[len(s)][len(t)]


# Space Optimized
# T.C. - O(N*M)
# S.C  - O(m)+O(n)


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [0 for _ in range(len(t) + 1)]

        for i in range(len(s) + 1):
            tmp = [0 for _ in range(len(t) + 1)]
            for j in range(len(t) + 1):
                if j == 0:
                    tmp[j] = 1
                elif i == 0:
                    tmp[j] = 0
                else:
                    if s[i - 1] == t[j - 1]:
                        tmp[j] = dp[j - 1] + dp[j]
                    else:
                        tmp[j] = dp[j]

            dp = tmp

        return dp[len(t)]
