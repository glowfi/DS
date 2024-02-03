# https://www.geeksforgeeks.org/problems/longest-common-substring1452/1 , Medium


# Tabulation
# T.C. - O(ind1*ind2)
# S.C  - O(ind1*ind2)


class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        dp = [[0 for _ in range(len(S2) + 1)] for _ in range(len(S1) + 1)]

        ans = 0

        for ind1 in range(len(S1) + 1):
            for ind2 in range(len(S2) + 1):
                if ind1 == 0 or ind2 == 0:
                    dp[ind1][ind2] = 0
                else:
                    match = 0
                    notMatch = 0
                    if S1[ind1 - 1] == S2[ind2 - 1]:
                        match = 1 + dp[ind1 - 1][ind2 - 1]
                    else:
                        notMatch = 0

                    dp[ind1][ind2] = max(match, notMatch)
                    ans = max(match, notMatch, ans)

        return ans


# Space Optimized
# T.C. - O(ind1*ind2)
# S.C  - O(ind2)


class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        dp = [0 for _ in range(len(S2) + 1)]
        ans = 0

        for ind1 in range(len(S1) + 1):
            tmp = [0 for _ in range(len(S2) + 1)]
            for ind2 in range(len(S2) + 1):
                if ind1 == 0 or ind2 == 0:
                    tmp[ind2] = 0
                else:
                    match, notMatch = 0, 0
                    if S1[ind1 - 1] == S2[ind2 - 1]:
                        match = 1 + dp[ind2 - 1]
                    else:
                        notMatch = 0

                    tmp[ind2] = max(match, notMatch)
                    ans = max(ans, match, notMatch)
            dp = tmp

        return ans
