# https://leetcode.com/problems/valid-parentheses/description/ , Medium

# Optimal
# T.C. - O(n)
# S.C  - O(n)+O(n)


class Solution:
    def isValid(self, s: str) -> bool:
        mp = {")": "(", "]": "[", "}": "{"}
        stk = []

        for i in range(len(s)):
            # Check top has coresspoding opening bracket or not
            if s[i] in mp:
                if stk and stk[-1] == mp[s[i]]:
                    stk.pop(-1)
                else:
                    return False
            else:
                # Appned if opening brackets
                stk.append(s[i])

        if len(stk) == 0:
            return True
        return False
