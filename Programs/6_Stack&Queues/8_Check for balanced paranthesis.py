# https://leetcode.com/problems/valid-parentheses , Easy

# Optimal
# T.C. - O(n)
# S.C  - O(n)+O(n)


class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {")": "(", "]": "[", "}": "{"}
        stk = []

        for i in range(len(s)):
            currChar = s[i]
            if currChar in bracketMap:
                if len(stk) > 0:
                    if stk[-1] != bracketMap[currChar]:
                        return False
                    else:
                        stk.pop(-1)
                else:
                    return False
            else:
                stk.append(currChar)

        return True if len(stk) == 0 else False
