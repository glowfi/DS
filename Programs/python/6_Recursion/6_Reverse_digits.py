# https://www.geeksforgeeks.org/problems/reverse-digit0316/1 , Easy, Recursion

# Question
# You are given an integer n. Your task is to reverse the digits, ensuring that the reversed number has no leading zeroes.

# Examples:

# Input: n = 122
# Output: 221
# Explanation: By reversing the digits of number, number will change into 221.

# Input : n = 200
# Output: 2
# Explanation: By reversing the digits of number, number will change into 2.

# Input : n = 12345
# Output: 54321
# Explanation: By reversing the digits of number, number will change into 54321.

# Constraints:
# 1 <= n <= 10^6


# Optimal
# T.C. - O(N)
# S.C  - O(N) [recursion stack space]

# Intuition
# Use Recursion and carry over the rev value in each recursive call


class Solution:
    def reverseDigits(self, n: int) -> int:
        def helper(rev: int, n: int) -> int:
            if n == 0:
                return rev

            d = n % 10
            return helper((rev * 10) + d, n // 10)

        return helper(0, n)
