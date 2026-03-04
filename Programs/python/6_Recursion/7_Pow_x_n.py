# https://leetcode.com/problems/powx-n, Medium, IBH

# Question
# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

# Example 1:

# Input: x = 2.00000, n = 10
# Output: 1024.00000
# Example 2:

# Input: x = 2.10000, n = 3
# Output: 9.26100
# Example 3:

# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25

# Constraints:

# -100.0 < x < 100.0
# -2^31 <= n <= 2^31-1
# n is an integer.
# Either x is not zero or n > 0.
# -10^4 <= xn <= 10^4

# Brute
# T.C. - O(1)
# S.C  - O(1)

# Intuition
# use inbuilt ** operator


class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n


# Optimal
# T.C. - O(log(n))
# S.C  - O(log(n))

# Intuition
# Use IBH method to solve this
# One pattern to notice that suppose we have an even power
# lets say 5**4 we just need to calculate 5**2 because to
# get the final 5**4 answer we just multiply result of 5**2
# by itself as 5^2 * 5^2 = 5^4.For odd power the same logic
# holds but we just need to add x to the final answer


class Solution:
    def solve(self, x: float, n: int) -> float:
        # Base
        if n == 0:
            return 1

        # Hypothesis
        res = self.solve(x, n // 2)

        # Induction
        if n % 2 == 0:
            return res * res

        return res * res * x

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.solve(x, -n)

        return self.solve(x, n)
