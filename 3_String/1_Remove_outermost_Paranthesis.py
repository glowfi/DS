# https://leetcode.com/problems/remove-outermost-parentheses/,Easy

# Optimal
# T.C. -> O(n)
# S.C. -> O(1)


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        depthCount = 0
        final = ""

        for i in range(len(s)):
            if s[i] == "(":
                depthCount += 1
            elif s[i] == ")":
                depthCount -= 1

            if depthCount == 1 and s[i] == "(":
                pass

            elif depthCount == 0 and s[i] == ")":
                pass

            else:
                final += s[i]

        return final
