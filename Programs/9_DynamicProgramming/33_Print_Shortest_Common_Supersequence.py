# https://leetcode.com/problems/shortest-common-supersequence/ , Hard


# Tabulation
# T.C. - O(m*m)+O(n*m)
# S.C  - O(n*m)+O(k)


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        dp = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]

        for i1 in range(len(str1) + 1):
            for i2 in range(len(str2) + 1):
                if i1 == 0 or i2 == 0:
                    dp[i1][i2] = 0
                else:
                    match, notMatch = 0, 0
                    if str1[i1 - 1] == str2[i2 - 1]:
                        match = 1 + dp[i1 - 1][i2 - 1]
                    else:
                        notMatch = max(dp[i1 - 1][i2], dp[i1][i2 - 1])

                    dp[i1][i2] = max(match, notMatch)

        i1, i2 = len(str1), len(str2)
        st = ""

        while i1 > 0 and i2 > 0:
            if str1[i1 - 1] == str2[i2 - 1]:
                st += str1[i1 - 1]
                i1 -= 1
                i2 -= 1
            elif dp[i1 - 1][i2] > dp[i1][i2 - 1]:
                st += str1[i1 - 1]
                i1 -= 1
            else:
                st += str2[i2 - 1]
                i2 -= 1

        while i1 > 0:
            st += str1[i1 - 1]
            i1 -= 1

        while i2 > 0:
            st += str2[i2 - 1]
            i2 -= 1

        return st[::-1]
