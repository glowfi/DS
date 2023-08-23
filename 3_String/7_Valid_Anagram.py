# https://leetcode.com/problems/valid-anagram/ , Easy

# Optimal
# T.C. -> O(n)
# S.C. -> O(n)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        h1, h2 = {}, {}

        for i in range(len(s)):
            currChar_s = s[i]
            currChar_t = t[i]

            if currChar_s not in h1:
                h1[currChar_s] = 1
            else:
                h1[currChar_s] += 1

            if currChar_t not in h2:
                h2[currChar_t] = 1
            else:
                h2[currChar_t] += 1

        return h1 == h2
