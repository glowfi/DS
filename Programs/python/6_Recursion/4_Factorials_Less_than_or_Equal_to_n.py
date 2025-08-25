# https://www.geeksforgeeks.org/problems/find-all-factorial-numbers-less-than-or-equal-to-n3548/1, Easy, Recursion

# Question
# A number n is called a factorial number if it is the factorial of a positive integer. For example,
# the first few factorial numbers are 1, 2, 6, 24, 120,
# Given a number n, the task is to return the list/vector of the factorial numbers smaller than or equal to n.

# Examples:

# Input: n = 3
# Output: 1 2
# Explanation: The first factorial number is 1 which is less than equal to n. The second number
# is 2 which is less than equal to n,but the third factorial number is 6 which is greater than n. So we print only 1 and 2.

# Input: n = 6
# Output: 1 2 6
# Explanation: The first three factorial numbers are less than equal to n but the fourth factorial
# number 24 is greater than n. So we print only first three factorial numbers.

# Constraints:
# 1<=n<=10^18

# Better
# T.C. - O(N)+O(N)
# S.C  - O(N) [recursion stack space] + O(N) [auxilairy space]

# Intuition
# Use Pure Recursion


class Solution:
    def factorialNumbers(self, n: int) -> list[int]:
        def solve(idx: int, n: int) -> list[int]:
            if idx > n:
                return []

            res = solve(idx + 1, n)

            if idx < n:
                res.append(idx)

            return res

        return solve(1, n)[::-1]


# Optimal
# T.C. - O(N)
# S.C  - O(N) [auxilairy space]

# Intuition
# Use Iterative method keeping track of the factorial


class Solution:
    def factorialNumbers(self, n: int) -> list[int]:
        ans = []

        p = 1
        for i in range(1, n + 1):
            p *= i

            if p > n:
                break
            else:
                ans.append(p)

        return ans
