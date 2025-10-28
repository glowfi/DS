# https://leetcode.com/problems/valid-palindrome, Easy, Two Pointers

# Question
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.


# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

# Brute
# T.C. - O(n)+O(n)
# S.C  - O(n)

# Intuition
# Create a new string considering only alpha numeric characters
# then reverse the new string and check whether it becomes the
# new string or not


class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_st = ""

        for i in range(len(s)):
            if s[i].isalnum():
                new_st += s[i].lower()

        return new_st[::-1] == new_st


# Optimal
# T.C. - O(n)
# S.C  - O(1)

# Intuition
# Fix 2 Pointers at the 2 ends of the given string
# Skip non alphanumeric from left and right
# if valid characters do not match return False


class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1, p2 = 0, len(s) - 1

        while p1 < p2:
            if not s[p1].isalnum():
                p1 += 1
                continue

            if not s[p2].isalnum():
                p2 -= 1
                continue

            if s[p1].lower() != s[p2].lower():
                return False

            p1 += 1
            p2 -= 1

        return True
