# https://leetcode.com/problems/roman-to-integer/ , Easy

# Optimal
# T.C. -> O(n)
# S.C. -> O(7)


class Solution:
    def romanToInt(self, s: str) -> int:
        mp = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        final = 0

        for i in range(len(s) - 1):
            if mp[s[i]] < mp[s[i + 1]]:
                final += (-1) * mp[s[i]]
            else:
                final += mp[s[i]]

        final += mp[s[-1]]

        return final
