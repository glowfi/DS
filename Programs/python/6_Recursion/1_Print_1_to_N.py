# https://www.geeksforgeeks.org/problems/print-1-to-n-without-using-loops3621/1 , Easy, IBH

# Question
# Given an positive integer n, print numbers from 1 to n without using loops.

# Implement the function printTillN() to print the numbers from 1 to n as space-separated integers.

# Examples

# Input: n = 5
# Output: 1 2 3 4 5
# Explanation: We have to print numbers from 1 to 5.

# Input: n = 10
# Output: 1 2 3 4 5 6 7 8 9 10
# Explanation: We have to print numbers from 1 to 10.

# Constraints:
# 1 ≤ n ≤ 1000

# Optimal
# T.C. - O(N)
# S.C  - O(N) [recursion stack space]

# Intuition
# Use the IBH method to solve this problem
# lets assume that printTillN will print from 1 to N as hypothesis
# assume N-1 will print from 1 to N-1 then in the induction step
# we can just print N at last


class Solution:
    def printTillN(self, N: int) -> None:
        # Base
        if N == 0:
            return

        # Hypo
        self.printTillN(N - 1)

        # Induction
        print(N, end=" ")
