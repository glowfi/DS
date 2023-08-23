# https://leetcode.com/problems/sum-of-beauty-of-all-substrings/ , Medium

# Optimal
# T.C. -> O(n*n)
# S.C. -> O(26)


class Solution:
    def getBeauty(self, s):
        h = {}
        m_f = float("-inf")
        l_f = float("inf")

        for i in s:
            h[i] = 1 + h.get(i, 0)

        for j in h:
            if h[j] > m_f:
                m_f = h[j]

            if h[j] < l_f:
                l_f = h[j]

        return m_f - l_f

    def beautySum(self, s: str) -> int:
        sm = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                sm += self.getBeauty(s[i : j + 1])
        return sm
