# https://www.geeksforgeeks.org/problems/palindrome0746/1, Easy, Recursion

# Question
# You are given an integer n. Your task is to determine whether it is a palindrome.

# A number is considered a palindrome if it reads the same backward as forward, like the string examples "MADAM" or "MOM".

# Examples:

# Input: n = 555
# Output: true
# Explanation: The number 555 reads the same backward as forward, so it is a palindrome.

# Input: n = 123
# Output: false
# Explanation: The number 123 reads differently backward (321), so it is not a palindrome.

# Input: n = 1221
# Output: true

# Constraints:
# 1 ≤ n ≤ 109

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

    def isPalindrome(self, n: int) -> bool:
        return self.reverseDigits(n) == n
