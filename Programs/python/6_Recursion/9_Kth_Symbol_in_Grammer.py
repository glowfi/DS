# https://leetcode.com/problems/k-th-symbol-in-grammar, Medium, IBH

# Question
# We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row,
# we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

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
# 1 <= k <= 2^n - 1

# Better
# T.C. - O(n)
# S.C  - O(n)

# Intuition
# Use IBH method to solve this problem
# One pattern to observe is that the current
# row is the combination of previous row and
# inverted previous row. See example below:
# 0
# 0 1
# 0 1 1 0
# 0 1 1 0 1 0 0 1
# 0 1 1 0 1 0 0 1 1 0 0 1 0 1 1 0
# the nth row has 2**(n-1) elements and
# if the k is larger than the mid then
# we return the abs(mid-k) from previous row
# oyherwise the kth result from previous row


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # Base
        if n == 1:
            return 0

        # Hypothesis & Induction
        total_elements = 2 ** (n - 1)
        mid = total_elements // 2
        if k <= mid:
            return self.kthGrammar(n - 1, k)

        return int(not (self.kthGrammar(n - 1, k - mid)))


# Optimal
# T.C. - O(n)
# S.C  - O(1)

# Intuition
# We start from backwards tracing upwards
# we assume that the answer is 1 and try to
# flip the symbol n of times and atlast if we
# and at the known symbol of zero at first row
# then we can say our assumption was right so
# we can return 1 otherwise return zero.
# At each iteration we move one row at a time
# backwards,fliping the assumption n number of times


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0

        symbol = 1

        for _ in range(n, 1, -1):
            total_elem = 2 ** (n - 1)
            mid = total_elem // 2

            if k > mid:
                symbol = 1 - symbol
                k = k - mid
            n -= 1

        if symbol != 0:
            return 0

        return 1
