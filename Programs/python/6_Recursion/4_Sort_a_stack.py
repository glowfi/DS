# https://www.geeksforgeeks.org/problems/sort-a-stack/1, Easy, IBH

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

# Brute
# T.C. - O(n^2)
# S.C  - O(n)

# Intuition
# Use the IBH method for sorting recursion
# H -> define sortStack will sort the stack given nums as the stack to sort
# B -> if n is less than equal to 1 just return stack
# I -> we using Hypothesis sort the stack from 1 to n-1 and then for the nth element
# we try to find its best insertion point using upper bound


from typing import List
from bisect import bisect_right


class Solution:
    def sortStack(self, st: List[int]):
        # Base
        if len(st) <= 1:
            return st

        # Hypothesis
        last_val = st.pop(-1)
        self.sortStack(st)

        # Induction
        best_idx = bisect_right(st, last_val)
        st.insert(best_idx, last_val)

        return st
