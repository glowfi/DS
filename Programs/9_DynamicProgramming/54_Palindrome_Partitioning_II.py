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
# T.C. - O(2^n)
# S.C  - O(n)


class Solution:
    def checkPalindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1

        return True

    def solve(self, i, j, s):
        if i >= j:
            return 0

        if self.checkPalindrome(s, i, j):
            return 0

        mn_cut = float("inf")

        for k in range(i, j):
            curr = self.solve(i, k, s) + self.solve(k + 1, j, s) + 1
            if curr < mn_cut:
                mn_cut = curr

        return mn_cut

    def minCut(self, s: str) -> int:
        return self.solve(0, len(s) - 1, s)


# Memoization
# T.C. - O(N^2)
# S.C  - O(N^3)+O(N)


class Solution:
    def checkPalindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1

        return True

    def solve(self, i, j, s, dp):
        if i >= j:
            return 0

        if self.checkPalindrome(s, i, j):
            return 0

        if (i, j) in dp:
            return dp[(i, j)]

        mn_cut = float("inf")

        for k in range(i, j):
            if (i, k) in dp:
                left = dp[(i, k)]
            else:
                left = self.solve(i, k, s, dp)
                dp[(i, k)] = left

            if (k + 1, j) in dp:
                right = dp[(k + 1, j)]
            else:
                right = self.solve(k + 1, j, s, dp)
                dp[(k + 1, j)] = right

            curr = left + right + 1
            if curr < mn_cut:
                mn_cut = curr

        dp[
            (
                i,
                j,
            )
        ] = mn_cut

        return mn_cut

    def minCut(self, s: str) -> int:
        return self.solve(0, len(s) - 1, s, {})


# Tabulation
# T.C. - O(N^3)
# S.C  - O(N^3)


class Solution:
    def checkPalindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1

        return True

    def minCut(self, s: str) -> int:
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]

        for i in range(len(s), -1, -1):
            for j in range(i + 1, len(s)):
                if self.checkPalindrome(s, i, j):
                    dp[i][j] = 0
                else:
                    mn_cut = float("inf")
                    for k in range(i, j):
                        curr = dp[i][k] + dp[k + 1][j] + 1
                        if curr < mn_cut:
                            mn_cut = curr
                    dp[i][j] = mn_cut

        return dp[0][len(s) - 1]
