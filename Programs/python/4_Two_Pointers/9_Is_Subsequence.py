# https://leetcode.com/problems/is-subsequence, Easy, Two Pointers

# Question
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false


# Constraints:
# 0 <= s.length <= 100
# 0 <= t.length <= 10^4
# s and t consist only of lowercase English letters.

# Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109,
# and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?

# Optimal
# T.C. - O(n)
# S.C  - O(1)

# Intuition
# Use two pointers p1 and p2
# p1 pointes to string s and p2 points to string t
# if a character at index p1 matches character at
# p2 we move p1 by one.At the end we check whether
# p1 reached its max length or not provind its a
# subsequence of t.


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1, p2 = 0, 0

        while p1 < len(s) and p2 < len(t):
            if t[p2] == s[p1]:
                p1 += 1
            p2 += 1

        return p1 == len(s)


# Optimal
# T.C. - O(t)+ O(|s| × log(|t|))*k
# S.C  - O(t)

# Intuition
# Pre process all the results
# for every string s map each character to t
# s such that they maintain relative order
# for already mapped character from s keep track
# of the index choosen , such that when a new
# character is going to me mapped we can verify
# that an index just greater than previous index
# exist by doing an upper bound check.Also keep
# updating the index at each step

import bisect
from collections import defaultdict


class Solution:
    def __init__(self) -> None:
        self.char_map = defaultdict(list)

    def pre_process(self, t: str):
        for idx, st in enumerate(t):
            self.char_map[st].append(idx)

    def isSubsequence(self, s: str):
        prev_idx = -1
        for i in range(len(s)):
            curr_char = s[i]

            if curr_char not in self.char_map:
                return False

            idx = bisect.bisect_right(self.char_map[curr_char], prev_idx)
            if idx == len(self.char_map[curr_char]):
                return False

            prev_idx = idx

        return True
