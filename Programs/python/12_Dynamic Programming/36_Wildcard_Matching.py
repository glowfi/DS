# https://leetcode.com/problems/wildcard-matching/ , Hard

# Recursion
# T.C. - 2^O(N*M)
# S.C  - O(N*M)+O(N+M)


class Solution:
    def solve(self, i, j, s, p):
        # Base Case
        if i == 0 and j == 0:
            return True

        elif i > 0 and j == 0:
            return False

        elif i == 0 and j > 0:
            for i in range(j):
                if p[i] != "*":
                    return False
            return True

        # Try out all possible ways
        if s[i - 1] == p[j - 1] or p[j - 1] == "?":
            return self.solve(i - 1, j - 1, s, p)

        elif p[j - 1] == "*":
            return self.solve(i, j - 1, s, p) or self.solve(i - 1, j, s, p)

        else:
            return False

    def isMatch(self, s: str, p: str) -> bool:
        return self.solve(len(s), len(p), s, p)


# Memoization
# T.C. - O(N*M)
# S.C  - O(N*M)+O(N+M)


class Solution:
    def solve(self, i, j, s, p, dp):
        if (i, j) in dp:
            return dp[(i, j)]
        # Base Case
        if i == 0 and j == 0:
            return True

        elif i > 0 and j == 0:
            return False

        elif i == 0 and j > 0:
            for i in range(j):
                if p[i] != "*":
                    return False
            return True

        # Try out all possible ways
        if s[i - 1] == p[j - 1] or p[j - 1] == "?":
            dp[(i, j)] = self.solve(i - 1, j - 1, s, p, dp)
            return dp[(i, j)]

        elif p[j - 1] == "*":
            dp[(i, j)] = self.solve(i, j - 1, s, p, dp) or self.solve(
                i - 1, j, s, p, dp
            )
            return dp[(i, j)]

        else:
            dp[(i, j)] = False
            return dp[(i, j)]

    def isMatch(self, s: str, p: str) -> bool:
        return self.solve(len(s), len(p), s, p, {})


# Tabulation
# T.C. - O(N*M)
# S.C  - O(N*M)


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]

        dp[0][0] = True

        # Fill first column with zero
        for row in range(len(s) + 1):
            dp[row][0] = False

        # Fill first row with zero
        for col in range(len(p) + 1):
            flag = False
            for k in range(col):
                if p[k] != "*":
                    flag = not flag
                    dp[0][col] = False
                    break
            if not flag:
                dp[0][col] = True

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == "?":
                    dp[i][j] = dp[i - 1][j - 1]

                elif p[j - 1] == "*":
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

                else:
                    dp[i][j] = False

        return dp[len(s)][len(p)]
