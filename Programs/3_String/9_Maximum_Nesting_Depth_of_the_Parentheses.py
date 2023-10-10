# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/ , Easy

# Optimal
# T.C. -> O(n)
# S.C. -> O(1)


class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        maxDepth = 0

        for i in s:
            if i == "(":
                depth += 1
            elif i == ")":
                depth -= 1

            maxDepth = max(depth, maxDepth)

        return maxDepth
