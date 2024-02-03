# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/ , Hard

# Intuition : Keep the longest palindromic susbequence intact because we need to minimize the no of insertion operations.
# Observations: str+rev(str) will make the string palindromic but that will be max operaions.
# Example: abcaa , codingninjas


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

    def minInsertions(self, s: str) -> int:
        return len(s) - self.longestPalindromeSubseq(s)
