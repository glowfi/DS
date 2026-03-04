# https://www.geeksforgeeks.org/problems/print-n-to-1-without-loop/0, Easy, IBH

# Question
# Print numbers from N to 1 (space separated) without the help of loops.

# Example 1:

# Input:
# N = 10
# Output: 10 9 8 7 6 5 4 3 2 1
# Your Task:
# This is a function problem. You only need to complete the function printNos() that
# takes N as parameter and prints number from N to 1 recursively. Don't print newline, it will be added by the driver code.

# Expected Time Complexity: O(N).
# Expected Auxiliary Space: O(N) (Recursive).

# Constraint
# 1<=n<=1000

# Optimal
# T.C. - O(n)
# S.C  - O(n)

# Intuition
# Use the IBH method for recursion
# H -> define printNos will n to 1 for the given n
# B -> if n is less than 1 just return
# I -> make the function print n-1 to n, we just print n


class Solution:
    def printNos(self, n):
        # Base
        if n < 1:
            return

        # Induction
        print(n, end=" ")

        # Hypothesis
        self.printNos(n - 1)
