# https://leetcode.com/problems/count-and-say, Medium, IBH

# Question
# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

# countAndSay(1) = "1"
# countAndSay(n) is the run-length encoding of countAndSay(n - 1).
# Run-length encoding (RLE) is a string compression method that works by replacing consecutive
# identical characters (repeated 2 or more times) with the concatenation of the character
# and the number marking the count of the characters (length of the run). For example,
# to compress the string "3322251" we replace "33" with "23", replace "222" with "32",
# replace "5" with "15" and replace "1" with "11". Thus the compressed string becomes "23321511".

# Given a positive integer n, return the nth element of the count-and-say sequence.

# Example 1:
# Input: n = 4
# Output: "1211"

# Explanation:

# countAndSay(1) = "1"
# countAndSay(2) = RLE of "1" = "11"
# countAndSay(3) = RLE of "11" = "21"
# countAndSay(4) = RLE of "21" = "1211"
# Example 2:

# Input: n = 1
# Output: "1"
# Explanation:
# This is the base case.

# Constraints:
# 1 <= n <= 30


# Better
# T.C. - O(n*m)
# S.C  - O(n)+O(m)

# Intuition
# Use IBH method to solve this problem.
# Create an get_encoding function that will give us the encoding.
# One thing to note to get current encoding we pass the result of
# previous to our function and we keep doing this n times.But we
# are going to use IBH method where in hypothesis step we try to
# find the previous value automatically and get the encoding from
# the previous value in the induction step


class Solution:
    def get_encoding(self, s: str) -> str:
        c = 1
        encoded = ""
        n = len(s)
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                encoded += f"{c}{s[i-1]}"
                c = 1
            else:
                c += 1

        return encoded + f"{c}{s[n-1]}"

    def countAndSay(self, n: int) -> str:
        # Base
        if n == 1:
            return "1"

        # Hypothesis
        prev_res = self.countAndSay(n - 1)

        # Induction
        return self.get_encoding(prev_res)


# Optimal
# T.C. - O(n*m)
# S.C  - O(m)

# Intuition
# Create an get_encoding function that will give us the encoding.
# One thing to note to get current encoding we pass the result of
# previous to our function and we keep doing this n times iteratively


class Solution:
    def get_encoding(self, s: str) -> str:
        c = 1
        encoded = ""
        n = len(s)
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                encoded += f"{c}{s[i-1]}"
                c = 1
            else:
                c += 1

        return encoded + f"{c}{s[n-1]}"

    def countAndSay(self, n: int) -> str:
        # Base
        if n == 1:
            return "1"

        # Hypothesis
        prev_res = self.countAndSay(n - 1)

        # Induction
        return self.get_encoding(prev_res)
