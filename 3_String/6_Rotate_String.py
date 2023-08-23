# https://leetcode.com/problems/rotate-string/ , Easy

# Optimal
# T.C. -> O(n)
# S.C. -> O(1)


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            rotated = s[i:] + s[:i]
            if rotated == goal:
                return True
        return False
