# https://www.geeksforgeeks.org/problems/print-n-to-1-without-loop/1, Easy, IBH

# Question
# Print numbers from N to 1 (space separated) without the help of loops.

# Example 1:

# Input:
# N = 10
# Output: 10 9 8 7 6 5 4 3 2 1
# Your Task:
# This is a function problem. You only need to complete
# the function printNos() that takes N as parameter and prints number
# from N to 1 recursively. Don't print newline, it will be added by the driver code.


# Expected Time Complexity: O(N).
# Expected Auxiliary Space: O(N) (Recursive).

# Constraint
# 1<=n<=1000

# Optimal
# T.C. - O(N)
# S.C  - O(N) [recursion stack space]

# Intuition
# Use the IBH method to solve this problem
# lets assume that printTillN will print from 1 to N as hypothesis
# we can just print N first
# assume N-1 will print from 1 to N-1 then in the induction step


class Solution:
    def printNos(self, n: int) -> None:
        # Base
        if n == 0:
            return

        # Induction
        print(n, end=" ")

        # Hypo
        self.printNos(n - 1)
