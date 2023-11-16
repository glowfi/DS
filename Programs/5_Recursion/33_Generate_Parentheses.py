# https://leetcode.com/problems/generate-parentheses/ , Medium

# Recursive Tree
# https://0x0.st/HtdN.306.png


# Optimal [ans in argument]
# T.C. - O(N*2^N)
# S.C  - O(N)


class Solution:
    def helper(self, opCount: int, clCount: int, n: int, proc: str, res: list[str]):
        if opCount == n and clCount == n:
            res.append(proc)

        if opCount < n:
            self.helper(opCount + 1, clCount, n, proc + "(", res)

        if clCount < opCount:
            self.helper(opCount, clCount + 1, n, proc + ")", res)

    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.helper(0, 0, n, "", res)
        return res


# Optimal [ans in body]
# T.C. - O(N*2^N)
# S.C  - O(N)


class Solution:
    def helper(self, opCount: int, clCount: int, n: int, proc: str) -> list[str]:
        if opCount == n and clCount == n:
            return [proc]

        tmp = []
        if opCount < n:
            val = self.helper(opCount + 1, clCount, n, proc + "(")
            for i in val:
                tmp.append(i)

        if clCount < opCount:
            val = self.helper(opCount, clCount + 1, n, proc + ")")
            for i in val:
                tmp.append(i)

        return tmp

    def generateParenthesis(self, n: int) -> List[str]:
        return self.helper(0, 0, n, "")
