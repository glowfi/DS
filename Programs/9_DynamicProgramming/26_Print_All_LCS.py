# https://www.geeksforgeeks.org/problems/print-all-lcs-sequences3413/1 , Hard


# Brute
# T.C. -
# S.C  -


class Solution:
    def backtrack(self, ind1, ind2, s1, s2, dp, ans, tmp):
        if ind1 == 0 or ind2 == 0:
            ans.add(tmp[::-1])
            return

        elif s1[ind1 - 1] == s2[ind2 - 1]:
            self.backtrack(ind1 - 1, ind2 - 1, s1, s2, dp, ans, tmp + s1[ind1 - 1])
        else:
            if dp[ind1 - 1][ind2] > dp[ind1][ind2 - 1]:
                self.backtrack(ind1 - 1, ind2, s1, s2, dp, ans, tmp)

            elif dp[ind1][ind2 - 1] > dp[ind1 - 1][ind2]:
                self.backtrack(ind1, ind2 - 1, s1, s2, dp, ans, tmp)

            else:
                self.backtrack(ind1 - 1, ind2, s1, s2, dp, ans, tmp)
                self.backtrack(ind1, ind2 - 1, s1, s2, dp, ans, tmp)

    def all_longest_common_subsequences(self, s, t):
        dp = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]

        for ind1 in range(len(s) + 1):
            for ind2 in range(len(t) + 1):
                if ind1 == 0 or ind2 == 0:
                    dp[ind1][ind2] = 0
                else:
                    match, notMatch = 0, 0
                    if s[ind1 - 1] == t[ind2 - 1]:
                        match = 1 + dp[ind1 - 1][ind2 - 1]
                    else:
                        notMatch = max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1])

                    dp[ind1][ind2] = max(match, notMatch)

        ans = set()
        self.backtrack(len(s), len(t), s, t, dp, ans, "")
        ans = list(ans)
        ans.sort()
        return ans
