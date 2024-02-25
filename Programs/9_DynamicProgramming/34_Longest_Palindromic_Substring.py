# https://leetcode.com/problems/longest-palindromic-substring/ , Medium


# Tabulation
# T.C. - O(n^2)
# S.C  - O(n^2)


class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]

        res = ""
        maxLen = 0

        for diff in range(len(s)):
            for i in range(len(s)):
                j = i + diff
                if j < len(s):
                    if i == j:
                        dp[i][j] = 1
                    elif diff == 1:
                        dp[i][j] = 2 if s[i] == s[j] else 0
                    else:
                        if s[i] == s[j] and dp[i + 1][j - 1]:
                            dp[i][j] = dp[i + 1][j - 1] + 2

                    if dp[i][j]:
                        if dp[i][j] > maxLen:
                            maxLen = dp[i][j]
                            res = s[i : i + diff + 1]

        return res
