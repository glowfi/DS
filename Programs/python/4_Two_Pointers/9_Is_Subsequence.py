# https://leetcode.com/problems/is-subsequence, Easy, Two Pointers

# Question
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by deleting
# some (can be none) of the characters without disturbing the relative positions of the
# remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

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
# We want to check if string s appears inside string t in the same order,
# but not necessarily contiguously. This is the definition of a subsequence.
#
# Use two pointers:
# - p1 for s
# - p2 for t
#
# Move p2 through t. Whenever s[p1] == t[p2], we advance p1 to look for
# the next character of s. p2 always moves forward.
#
# If by the end p1 has reached len(s), it means we successfully matched
# every character of s in order within t, so s is a subsequence of t.
# Otherwise, some character of s could not be matched and the answer is False.


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
# Since t is fixed we can do some pre-computation,
# we are going to build a hashmap table where key
# is the character in string t and value is the list
# of indices of that character.
# We are going to keep track of index mapped from
# string t as we proceed
# For each character of s we are going to check if it
# is present in the table or not,if present we are
# going to check if we are able to find an index
# greater than last index.


import bisect
from collections import defaultdict


class SubsequenceCheckerBinarySearch:
    def __init__(self, t: str):
        self.char_indices = defaultdict(list)

        for i, char in enumerate(t):
            self.char_indices[char].append(i)

    def isSubsequence(self, s: str) -> bool:
        last_index = -1

        for i in range(len(s)):
            chr = s[i]
            if chr not in self.char_indices:
                return False

            next_index = bisect.bisect_right(self.char_indices[chr], last_index)
            if next_index == len(self.char_indices[chr]):
                return False

            last_index = self.char_indices[chr][next_index]

        return True


t = "ahbgdc"
checker = SubsequenceCheckerBinarySearch(t)

print(checker.isSubsequence("abc"))  # True
print(checker.isSubsequence("axc"))  # False
print(checker.isSubsequence(""))  # True
print(checker.isSubsequence("ahbgdc"))  # True
