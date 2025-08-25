# https://leetcode.com/problems/k-th-symbol-in-grammar, Medium, IBH

# Question
# We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

# For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
# Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.


# Example 1:

# Input: n = 1, k = 1
# Output: 0
# Explanation: row 1: 0

# Example 2:

# Input: n = 2, k = 1
# Output: 0
# Explanation:
# row 1: 0
# row 2: 01

# Example 3:

# Input: n = 2, k = 2
# Output: 1
# Explanation:
# row 1: 0
# row 2: 01


# Constraints:

# 1 <= n <= 30
# 1 <= k <= 2^(n - 1)

# Brute
# T.C. - O(2^N)
# S.C  - O(N) [recursion stack space]

# Intuition
# Try using the IBH method
# Assume solve will return us the nth row given n
# Solve for smaller input of n-1, then use the result
# of n-1 to buidl the final nth row output


class Solution:
    def helper(self, num):
        mp = {"0": "01", "1": "10"}
        res = ""

        for n in num:
            res += mp[n]

        return res

    def kthGrammar(self, n: int, k: int) -> int:
        def solve(n):
            # Base
            if n == 1:
                return "0"

            # Hypo
            val = solve(n - 1)

            # Induction
            return self.helper(val)

        return int(solve(n)[k - 1])


# Optimal
# T.C. - O(log(N))
# S.C  - O(1)

# Intuition
# This question is completely observation based
# There are some observation which are given below:
# + if you are at nth row then it has 2**(n-1) elements
# + if you are looking for kth element then if the k lies
# before mid then its the kth element from prev row otherwise
# if it lies after mid its the not of k-mid of prev row
# We can use the concept of IBH and develop a hyp that
# given n and k kthGrammar function will return us the kth
# element in nth row
#
# Demo of first 4 rows:
# 0
#
# 0 1
# - -
#
# 0 1 1 0
# --- ---
#
# 0 1 1 0 1 0 0 1
# ------  ------


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1 and k == 1:
            return 0

        total_elem = 2 ** (n - 1)
        mid = total_elem // 2

        if k <= mid:
            return self.kthGrammar(n - 1, k)

        return int(not self.kthGrammar(n - 1, abs(mid - k)))
