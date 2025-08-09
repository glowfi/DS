# https://leetcode.com/problems/largest-odd-number-in-string , Easy, Basic

# Question
# You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that
# is a non-empty substring of num, or an empty string "" if no odd integer exists.
# A substring is a contiguous sequence of characters within a string.

# Example 1:

# Input: num = "52"
# Output: "5"
# Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.
# Example 2:

# Input: num = "4206"
# Output: ""
# Explanation: There are no odd numbers in "4206".
# Example 3:

# Input: num = "35427"
# Output: "35427"
# Explanation: "35427" is already an odd number.


# Constraints:

# 1 <= num.length <= 10^5
# num only consists of digits and does not contain any leading zeros.


# Optimal
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# An odd number ends with either 1,3,5,7,9
# we want the largest-valued odd number in
# the string, so if we traverse from back of the string
# and find the first number that is not divisible by
# 2 that will give us the larges possible odd number
# substring from the given input string


class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 != 0:
                return num[: i + 1]
        return ""
