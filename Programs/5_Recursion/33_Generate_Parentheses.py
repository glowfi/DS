# https://leetcode.com/problems/generate-parentheses/ , Medium

# Brute
# T.C. - O(N*2^N)
# S.C  - O(N)


class Solution:
    def helper(self, openCount, closeCount, n, tmp, res):
        if openCount == n and closeCount == n:
            res.append(tmp)
            return

        if openCount < n:
            self.helper(openCount + 1, closeCount, n, tmp + "(", res)

        if closeCount < openCount:
            self.helper(openCount, closeCount + 1, n, tmp + ")", res)

    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.helper(0, 0, n, "", res)
        return res
