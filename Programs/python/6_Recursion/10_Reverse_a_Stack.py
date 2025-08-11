# https://www.geeksforgeeks.org/problems/reverse-a-stack/1, Easy, IBH

# Question
# You are given a stack St. You have to reverse the stack using recursion.

# Example 1:

# Input: St = [3,2,1,7,6]
# Output: [6,7,1,2,3]
# Explanation: Input stack after reversing will look like the stack in the output.
# Example 2:

# Input: St = [4,3,9,6]
# Output: [6,9,3,4]
# Explanation: Input stack after reversing will look like the stack in the output.

# Constraints:
# 1 ≤ stack.size ≤ 10^4
# 0 ≤ stack.element ≤ 10^3

# Brute
# T.C. - O(N^2)
# S.C  - O(1)

# Intuition
# Use IBH method to solve this problem
# Assume that in tht reversal function will
# reverse any given array(hypothesis),try reversing
# the entire array except the last element then at the
# induction step we just need to insert the last element
# to the front


class Solution:
    def reverse(self, st: list[int]) -> list[int]:
        # Base
        if len(st) == 0:
            return st

        # Hypothesis
        last_elem = st.pop(-1)
        self.reverse(st)

        # Induction
        st.insert(0, last_elem)

        return st
