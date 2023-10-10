# https://leetcode.com/problems/isomorphic-strings/ , Easy

# Optimal
# T.C. -> O(n1)
# S.C. -> O(n1+n2)


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        h1, h2 = {}, {}

        for i in range(len(s)):
            currChar_s = s[i]
            currChar_t = t[i]

            if (currChar_s in h1 and h1[currChar_s] != currChar_t) or (
                currChar_t in h2 and h2[currChar_t] != currChar_s
            ):
                return False
            else:
                h1[currChar_s] = currChar_t
                h2[currChar_t] = currChar_s

        return True
