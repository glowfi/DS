# https://leetcode.com/problems/remove-outermost-parentheses, Easy, Parentheses

# Question
# A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.

# For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
# A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

# Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

# Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.


# Example 1:

# Input: s = "(()())(())"
# Output: "()()()"
# Explanation:
# The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
# After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
# Example 2:

# Input: s = "(()())(())(()(()))"
# Output: "()()()()(())"
# Explanation:
# The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
# After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
# Example 3:

# Input: s = "()()"
# Output: ""
# Explanation:
# The input string is "()()", with primitive decomposition "()" + "()".
# After removing outer parentheses of each part, this is "" + "" = "".


# Constraints:

# 1 <= s.length <= 10^5
# s[i] is either '(' or ')'.
# s is a valid parentheses string.


# Optimal
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# Suppose we have an input case : s = "(()())(())(()(()))"

# (()()) Part1
# 121210

# (()) Part2
# 1210

# (()(())) Part3
# 12123210

# There is a pattern,
# + if depth count is 1 and if its opening brace then it is the outermost opening brace
# + if depth count is 0 and its closing brace, it is the outermost closing brace


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        depthCount: int = 0
        res: str = ""

        for char in s:

            if char == "(":
                depthCount += 1

            elif char == ")":
                depthCount -= 1

            if depthCount == 1 and char == "(":
                continue

            if depthCount == 0 and char == ")":
                continue

            res += char

        return res
