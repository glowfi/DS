# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses , Easy, Parentheses

# Question
# Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.


# Example 1:

# Input: s = "(1+(2*3)+((8)/4))+1"

# Output: 3

# Explanation:

# Digit 8 is inside of 3 nested parentheses in the string.

# Example 2:

# Input: s = "(1)+((2))+(((3)))"

# Output: 3

# Explanation:

# Digit 3 is inside of 3 nested parentheses in the string.

# Example 3:

# Input: s = "()(())((()()))"

# Output: 3


# Constraints:

# 1 <= s.length <= 100
# s consists of digits 0-9 and characters '+', '-', '*', '/', '(', and ')'.
# It is guaranteed that parentheses expression s is a VPS.


# Optimal
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# maintain a depth count
# if its an open parentheses add one
# if its a closed parentheses decrement one
# the max count throught the process will be the max depth


class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        max_depth = 0

        for char in s:
            if char == "(":
                depth += 1
            elif char == ")":
                depth -= 1
            max_depth = max(max_depth, depth)

        return max_depth
