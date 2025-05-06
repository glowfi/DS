# https://leetcode.com/problems/assign-cookies/ , Easy


# Optimal
# T.C. - O(nlog(n))+O(nlog(n))
# S.C  - O(1)

# Selection criteria : To satisfy as many children as possible, we want to assign the smallest sufficient cookie to the least greedy child
# Intuition : since the array is sorted we always move the cookie by one as if the current child is not satisfied, then next greater
# child will not be stasified too with the current cookie value so we can move both i and j pointer


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        i, j = 0, 0
        c = 0

        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
                j += 1
                c += 1
            else:
                j += 1

        return c
