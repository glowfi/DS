# https://www.geeksforgeeks.org/problems/sum-of-digits1742/1, Easy, IBH

# Question
# Given a positive number n. Find the sum of all the digits of n.

# Examples:

# Input: n = 687
# Output: 21
# Explanation: Sum of 687's digits: 6 + 8 + 7 = 21

# Input: n = 12
# Output 3
# Explanation: Sum of 12's digits: 1 + 2 = 3

# Constraints:
# 1 <= n <= 10^5


# Optimal
# T.C. - O(N)
# S.C  - O(N) [recursion stack space]

# Intuition
# Use IBH method to solve the problem
# Assum given n it will return the sum of the
# all digits in n (hypothesis),then recursively
# find the sum of x-1 digits (if number is 3 digit)
# then find sum of 2 digits and then add the last digit
# to the sum of x-1 digits and return this (induction)


class Solution:
    def sumOfDigits(self, n: int) -> int:
        # Base
        if n == 0:
            return 0

        # Hypo
        s = self.sumOfDigits(n // 10)

        # Induction
        return s + n % 10
