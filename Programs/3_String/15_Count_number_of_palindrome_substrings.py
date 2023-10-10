# https://leetcode.com/problems/palindromic-substrings/ , Medium

# Brute
# T.C. -> O(n*n)
# S.C. -> O(1)


class Solution:
    def countSubstrings(self, s: str) -> str:
        ans = ""
        c = 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                curr = s[i : j + 1]

                if curr == curr[::-1]:
                    c += 1

        return c


# Optimal
# T.C. -> O(n^2)
# S.C. -> O(1)


class Solution:
    def countSubstrings(self, s: str) -> str:
        c = 0

        for i in range(len(s)):
            # Even Length string
            l, r = i, i + 1
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break

                c += 1
                l -= 1
                r += 1

            # Odd Length string
            l, r = i, i
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break

                c += 1
                l -= 1
                r += 1

        return c
