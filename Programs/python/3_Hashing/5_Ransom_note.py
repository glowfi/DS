# https://leetcode.com/problems/ransom-note, Easy, HashMap / Frequency Count

# Question
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.


# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true

# Constraints:
# 1 <= ransomNote.length, magazine.length <= 10^5
# ransomNote and magazine consist of lowercase English letters.


# Optimal
# T.C. - O(n)+O(n) ~ O(n)
# S.C  - O(n)

# Intuition
# First store the frequency map of each character for magazine
# Now iterate over the ransomNote string and decrement the coresponding
# character by 1 and if at any point we say the current char is not present
# or no characters left we can return False


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mp = {}
        for i in range(len(magazine)):
            mp[magazine[i]] = 1 + mp.get(magazine[i], 0)

        for j in range(len(ransomNote)):
            if ransomNote[j] not in mp:
                return False

            if mp[ransomNote[j]] == 0:
                return False

            mp[ransomNote[j]] -= 1

        return True
