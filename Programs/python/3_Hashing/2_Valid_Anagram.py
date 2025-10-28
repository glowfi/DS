# https://leetcode.com/problems/valid-anagram, Easy, HashMap / Frequency Count

# Question
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.


# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false


# Constraints:

# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.


# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?


# Optimal
# T.C. - O(s+t)
# S.C  - O(s+t)

# Intuition
# Maintain a counter map
# store the frequency of each character for string s
# decrement the coresspoding character for string t in counter map
# validate couter map has all value as zero


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter_map = {}

        for i in range(len(s)):
            counter_map[s[i]] = 1 + counter_map.get(s[i], 0)

        for j in range(len(t)):
            ch = t[j]

            if ch not in counter_map:
                return False

            counter_map[ch] -= 1

        for _, val in counter_map.items():
            if val != 0:
                return False

        return True
