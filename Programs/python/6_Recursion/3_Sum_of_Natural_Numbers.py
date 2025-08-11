# https://www.geeksforgeeks.org/problems/sum-of-series2811/1, Easy, IBH

# Question
# Given an integer n, your task is to compute the sum of all natural numbers from 1 to n (inclusive). If n is 0, the sum should be 0.

# Examples:

# Input: n = 3
# Output: 6
# Explanation: For n = 3, the sum will be 6. 1 + 2 + 3 = 6.

# Input: n = 5
# Output: 15
# Explanation: For n = 5, the sum will be 15. 1 + 2 + 3 + 4 + 5 = 15.

# Constraints:
# 1 ≤ n ≤ 10^4

# Expected Complexities
# Time Complexity: O(1)
# Auxiliary Space: O(1)


# Better
# T.C. - O(N)
# S.C  - O(N) [recursion stack space]

# Intuition
# Use the IBH method to solve this problem
# As hypothesis assume that given n findSum function
# will calulcate the sum of 1 to n,first calulcate the
# sum of n-1 numbers then we can just add the current number
# with the result of n-1 sum (induction)


class Solution:
    def findSum(self, n: int) -> int:
        # Base
        if n == 0:
            return 0

        # Hypo
        sum_till_prev_num = self.findSum(n - 1)

        # Induction
        return sum_till_prev_num + n
