# https://www.geeksforgeeks.org/problems/minimum-number-of-deletions-and-insertions0209/1 , Medium


# Example: heap->pea
# Intuition-> s2 will give insertions , s1 will give deletions , some portion of the string remains intact in the s2


# Space Optimized
# T.C. - O(ind1*ind2)
# S.C  - O(ind2)


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
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

    def minOperations(self, s1, s2):
        lcs = self.longestCommonSubsequence(s1, s2)
        insert_operation = len(s2) - lcs
        delete_operation = len(s1) - lcs

        return insert_operation + delete_operation
