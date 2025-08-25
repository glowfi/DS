# https://leetcode.com/problems/powx-n/, Medium, IBH

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
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# Just multiply the number n times and return


class Solution:
    def myPow(self, x: float, n: int) -> float:
        p = 1

        for i in range(n):
            p *= x

        return p


# Better
# T.C. - O(log(N))
# S.C  - O(N) [recursion stack space]

# Intuition
# For even we know that 2**4 -> 2**2 * 2**2
# For odd we know that 2**5 -> 2* 2**2 * 2**2
# We just need to find the x**n//2 in each step
# and then multiply it with itself and if odd also
# multiply x


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x: float, n: int) -> float:
            if n == 0:
                return 1

            res = self.myPow(x, n // 2)
            if n % 2 == 0:
                return res * res

            return x * res * res

        if n < 0:
            return 1 / pow(x, -n)
        return pow(x, n)


# Optimal
# T.C. - O(log(N))
# S.C  - O(1)

# Intuition
# Square the base and half the exponent in each step
# For example to find 2^8
# (4^2)^8/2
# (16^2)^4/2
# (256)^2/2


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x: float, n: int) -> float:
            res = 1
            while n > 0:
                if n % 2 == 1:
                    res *= x
                x *= x
                n = n // 2
            return res

        if n < 0:
            return 1 / pow(x, -n)
        return pow(x, n)
