# https://leetcode.com/problems/valid-anagram , Easy, SpecialString

# Question
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.


# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false


# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.


# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?


# Optimal
# T.C. - O(S)
# S.C  - O(S)+O(T)

# Intuition
# Just compare the frequency map of
# the 2 strings


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq_map_s = {}
        freq_map_t = {}

        for i in range(len(s)):
            freq_map_s[s[i]] = 1 + freq_map_s.get(s[i], 0)
            freq_map_t[t[i]] = 1 + freq_map_t.get(t[i], 0)

        return freq_map_s == freq_map_t
