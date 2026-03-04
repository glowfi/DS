# https://www.geeksforgeeks.org/problems/print-1-to-n-without-using-loops-1587115620/1, Easy, IBH

# Question
# You are given an integer n. You have  to print all numbers from 1 to n.
# Note: You must use recursion only, and print all numbers from 1 to n in a single line, separated by spaces.

# Examples:

# Input: n = 10
# Output: 1 2 3 4 5 6 7 8 9 10

# Input: n = 5
# Output: 1 2 3 4 5

# Input: n = 1
# Output: 1

# Constraints:
# 1 ≤ n ≤ 10^3

# Optimal
# T.C. - O(n)
# S.C  - O(n)

# Intuition
# Use the IBH method for recursion
# H -> define printNos will 1 to n for the given n
# B -> if n is less than 1 just return
# I -> make the function print 1 to n-1, we just print n


class Solution:
    def printNos(self, n):
        # Base
        if n < 1:
            return

        # Hypothesis
        self.printNos(n - 1)

        # Induction
        print(n, end=" ")
