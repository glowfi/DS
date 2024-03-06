# https://leetcode.com/problems/palindrome-partitioning-ii/ , Hard


# Backtracking
# T.C. - O(2^n)
# S.C  - O(n)+O(n)


class Solution:
    def isPalindrome(self, s):
        return s == s[::-1]

    def solve(self, c, st, en, s, dp):

        if st >= en:
            return c - 1

        if (c, st, en) in dp:
            return dp[(c, st, en)]

        mn = float("inf")

        for i in range(st, en):
            first = s[st : i + 1]
            if self.isPalindrome(first):
                mn = min(self.solve(c + 1, i + 1, en, s, dp), mn)

        dp[(c, st, en)] = mn

        return dp[(c, st, en)]

    def minCut(self, s: str) -> int:
        return self.solve(0, 0, len(s), s, {})


# Recursion
# T.C. -
# S.C  -

# Memoization
# T.C. -
# S.C  -

# Tabulation
# T.C. -
# S.C  -

# Space Optimized
# T.C. -
# S.C  -
