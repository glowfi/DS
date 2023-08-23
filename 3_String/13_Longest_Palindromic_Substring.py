# https://leetcode.com/problems/longest-palindromic-substring/ , Medium

# Brute
# T.C. -> O(n*n)
# S.C. -> O(1)


class Solution:
    def longestPalindrome(self, s: str) -> str:
        mx = 0
        ans = ""

        for i in range(len(s)):
            for j in range(i, len(s)):
                curr = s[i : j + 1]

                if curr == curr[::-1]:
                    if len(curr) > mx:
                        mx = len(curr)
                        ans = curr

        return ans


# Optimal
# T.C. -> O(n^2)
# S.C. -> O(1)


class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        mx = 0

        for i in range(len(s)):
            # Even Length string
            l, r = i, i + 1
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break

                if r - l + 1 > mx:
                    mx = r - l + 1
                    ans = s[l : r + 1]

                l -= 1
                r += 1

            # Odd Length string
            l, r = i, i
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break

                if r - l + 1 > mx:
                    mx = r - l + 1
                    ans = s[l : r + 1]

                l -= 1
                r += 1

        return ans
