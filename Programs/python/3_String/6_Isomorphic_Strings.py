# https://leetcode.com/problems/isomorphic-strings , Easy, SpecialString

# Question
# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters.
# No two characters may map to the same character, but a character may map to itself.


# Example 1:

# Input: s = "egg", t = "add"

# Output: true

# Explanation:

# The strings s and t can be made identical by:

# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.
# Example 2:

# Input: s = "foo", t = "bar"

# Output: false

# Explanation:

# The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

# Example 3:

# Input: s = "paper", t = "title"

# Output: true


# Constraints:

# 1 <= s.length <= 5 * 10^4
# t.length == s.length
# s and t consist of any valid ascii character.


# Optimal
# T.C. - O(N)
# S.C  - O(2N)

# Intuition
# Just keep 2 hashmaps and assign a char of s to t and vice versa
# if a already assigned char from c does not matches with
# t and vice versa, return False otherwise at the end return True


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        cmap1, cmap2 = {}, {}

        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]

            if (c1 in cmap1 and cmap1[c1] != c2) or (c2 in cmap2 and cmap2[c2] != c1):
                return False

            cmap1[c1] = c2
            cmap2[c2] = c1

        return True
