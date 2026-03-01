# https://www.geeksforgeeks.org/problems/reverse-a-stack/1, Medium, IBH

# Question
# You are given a stack st[]. You have to reverse the stack.

# Note: The input array represents the stack from bottom to top (last element is the top).
# The output is displayed by printing elements from top to bottom after reversal.

# Examples:
# Input: st[] = [1, 2, 3, 4]
# Output: [1, 2, 3, 4]
# Explanation: After reversing, the elements of stack are in opposite order.

# Input: st[] = [3, 2, 1]
# Output: [3, 2, 1]
# Explanation: After reversing, the elements of stack are in opposite order.

# Constraints:
# 1 ≤ st.size() ≤ 100
# 0 ≤ stack element ≤ 100

# Brute
# T.C. - O(n^2)
# S.C  - O(n)

# Intuition
# Use the IBH method
# H -> define reverseStack will reverse any given stack
# B -> if stack empty we return stack
# I -> we using Hypothesis pop the top element and we reverse
# the stack from 0 to n-1 then atlast the top is inserted at the
# 0th index as on revesing it ends up as the bottom-most element

from typing import List


class Solution:
    def reverseStack(self, st: List[int]) -> List[int]:
        # Base
        if len(st) == 0:
            return st

        # Hypothesis
        top_elem = st.pop(-1)
        self.reverseStack(st)

        # Induction
        st.insert(0, top_elem)
        return st
