# https://leetcode.com/problems/reverse-words-in-a-string/,Medium

# Brute
# T.C. -> O(n)
# S.C. -> O(1)


class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.lstrip(" ")
        s = s.rstrip(" ")
        s = s.split()[::-1]
        return " ".join(s)


# Optimal
# T.C. -> O(n*k)
# S.C. -> O(n)+O(n)


class Solution:
    def reverseWords(self, s: str) -> str:
        s = " " + s
        s = s.rstrip(" ")
        idx = len(s) - 1
        final, tmp = "", ""

        while idx >= 0:
            if s[idx] != " ":
                tmp += s[idx]

            elif s[idx] == " " and s[idx - 1] != " ":
                final += tmp[::-1] + " "
                tmp = ""

            idx -= 1

        return final.rstrip(" ")
