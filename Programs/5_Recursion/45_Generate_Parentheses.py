# https://leetcode.com/problems/generate-parentheses/ , Medium

# Recursive Tree
# https://0x0.st/HtdN.306.png


# Optimal [ans in argument]
# T.C. - O(N*2^N)
# S.C  - O(N)


class Solution:
    def helper(self, op, cl, n, tmp, ans):
        if op == n and cl == n:
            ans.append(tmp[:])
            return

        if op < n:
            self.helper(op + 1, cl, n, tmp + "(", ans)

        if cl < op:
            self.helper(op, cl + 1, n, tmp + ")", ans)

    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.helper(0, 0, n, "", ans)
        return ans


# Optimal [ans in body]
# T.C. - O(N*2^N)
# S.C  - O(N)


class Solution:
    def helper(self, op, cl, n, tmp):
        if op == n and cl == n:
            return [tmp[:]]

        ans = []

        if op < n:
            vals = self.helper(op + 1, cl, n, tmp + "(")
            for val in vals:
                ans.append(val)

        if cl < op:
            vals = self.helper(op, cl + 1, n, tmp + ")")
            for val in vals:
                ans.append(val)

        return ans

    def generateParenthesis(self, n: int) -> List[str]:
        return self.helper(0, 0, n, "")
