# https://leetcode.com/problems/rotate-string, Easy, Rotation

# Question
# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

# A shift on s consists of moving the leftmost character of s to the rightmost position.

# For example, if s = "abcde", then it will be "bcdea" after one shift.


# Example 1:

# Input: s = "abcde", goal = "cdeab"
# Output: true
# Example 2:

# Input: s = "abcde", goal = "abced"
# Output: false


# Constraints:

# 1 <= s.length, goal.length <= 100
# s and goal consist of lowercase English letters.

# Brute
# T.C. - O(N^2)
# S.C  - O(1)

# Intuition
# Keep rotating the string by 1
# if at any point we reach the goal string return True


class Solution:
    def rotate_by_one(self, s: list[str]) -> str:
        for i in range(len(s) - 1):
            s[i], s[i + 1] = s[i + 1], s[i]
        return "".join(s)

    def rotateString(self, s: str, goal: str) -> bool:
        for _ in range(len(s)):
            s = self.rotate_by_one(list(s))
            if s == goal:
                return True

        return False


# Optimal
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# double concatentate the input string
# and check whether the goal exits in the
# concatentated string


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        concatenated = s + s

        return concatenated.find(goal) != -1
