# https://leetcode.com/problems/count-and-say, Medium, IBH

# Question
# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

# countAndSay(1) = "1"
# countAndSay(n) is the run-length encoding of countAndSay(n - 1).
# Run-length encoding (RLE) is a string compression method that works by replacing consecutive
# identical characters (repeated 2 or more times) with the concatenation of the character and
# the number marking the count of the characters (length of the run). For example, to
# compress the string "3322251" we replace "33" with "23", replace "222" with "32",
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


# Optimal
# T.C. - O(2^N)
# S.C  - O(N)+O(2^N) [recursion stack space]

# Intuition
# Think that a function fn given a n will return its encoding,
# try running the function for smaller n say n-1 (hypo)
# if we get the final result for n-1 then we are left to calculate
# the encoding for n with the result of n-1 (induction).if n is 1
# we can simpy return "1"


class Solution:
    def get_encoding(self, s: str) -> str:
        res = ""

        c = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                c += 1
            else:
                res += f"{c}{s[i-1]}"
                c = 1

        # Account the last number
        res += f"{c}{s[-1]}"

        return res

    def countAndSay(self, n: int) -> str:
        # Base
        if n == 1:
            return "1"

        # Hypo
        res = self.countAndSay(n - 1)

        # Induction
        return self.get_encoding(res)
