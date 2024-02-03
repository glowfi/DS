# https://leetcode.com/problems/longest-palindromic-subsequence/ , Medium

# Recursion
# T.C. - O(2^n*ind1*ind2)
# S.C  - O(min(ind1,ind2))


class Solution:
    def solve(self, ind1, ind2, s1, s2):
        if ind1 == 0 or ind2 == 0:
            return 0

        # If character matches
        match, notMatch = 0, 0
        if s1[ind1 - 1] == s2[ind2 - 1]:
            match = 1 + self.solve(ind1 - 1, ind2 - 1, s1, s2)

        # If not matches
        else:
            notMatch = max(
                self.solve(ind1 - 1, ind2, s1, s2), self.solve(ind1, ind2 - 1, s1, s2)
            )

        return max(match, notMatch)

    def longestPalindromeSubseq(self, s: str) -> int:
        return self.solve(len(s), len(s), s, s[::-1])


# Memoization
# T.C. - O(2^n*ind1*ind2)
# S.C  - O(min(ind1,ind2)) +O(ind1*ind2)


class Solution:
    def solve(self, ind1, ind2, s1, s2, dp):
        if (ind1, ind2) in dp:
            return dp[(ind1, ind2)]

        if ind1 == 0 or ind2 == 0:
            return 0

        # If character matches
        match, notMatch = 0, 0
        if s1[ind1 - 1] == s2[ind2 - 1]:
            match = 1 + self.solve(ind1 - 1, ind2 - 1, s1, s2, dp)

        # If not matches
        else:
            notMatch = max(
                self.solve(ind1 - 1, ind2, s1, s2, dp),
                self.solve(ind1, ind2 - 1, s1, s2, dp),
            )

        dp[(ind1, ind2)] = max(match, notMatch)
        return dp[(ind1, ind2)]

    def longestPalindromeSubseq(self, s: str) -> int:
        dp = {}
        return self.solve(len(s), len(s), s, s[::-1], dp)


# Tabulation
# T.C. - O(ind1*ind2)
# S.C  - O(ind1*ind2)


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        text1, text2 = s, s[::-1]
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

        for ind1 in range(len(text1) + 1):
            for ind2 in range(len(text2) + 1):
                if ind1 == 0 or ind2 == 0:
                    dp[ind1][ind2] = 0
                else:
                    match, notMatch = 0, 0
                    if text1[ind1 - 1] == text2[ind2 - 1]:
                        match = 1 + dp[ind1 - 1][ind2 - 1]
                    else:
                        notMatch = max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1])

                    dp[ind1][ind2] = max(match, notMatch)

        return dp[len(text1)][len(text2)]


# Space Optimized
# T.C. - O(ind1*ind2)
# S.C  - O(ind2)


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        text1, text2 = s, s[::-1]
        dp = [0 for _ in range(len(text2) + 1)]

        for ind1 in range(len(text1) + 1):
            tmp = [0 for _ in range(len(text2) + 1)]
            for ind2 in range(len(text2) + 1):
                if ind1 == 0 or ind2 == 0:
                    tmp[ind2] = 0
                else:
                    match, notMatch = 0, 0
                    if text1[ind1 - 1] == text2[ind2 - 1]:
                        match = 1 + dp[ind2 - 1]
                    else:
                        notMatch = max(dp[ind2], tmp[ind2 - 1])

                    tmp[ind2] = max(match, notMatch)
            dp = tmp

        return dp[len(text2)]
