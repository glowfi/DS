# https://www.geeksforgeeks.org/problems/delete-middle-element-of-a-stack/1, Easy, IBH

# Question
# Given a stack s, delete the middle element of the stack without using any additional data structure.

# Middle element:- floor((size_of_stack+1)/2) (1-based indexing) from the bottom of the stack.

# Note: The output shown by the compiler is the stack from top to bottom.

# Examples:

# Input: s = [10, 20, 30, 40, 50]
# Output: [50, 40, 20, 10]
# Explanation: The bottom-most element will be 10 and the top-most element
# will be 50. Middle element will be element at index 3 from bottom, which is 30. Deleting 30, stack will look like {10 20 40 50}.

# Input: s = [10, 20, 30, 40]
# Output: [40, 30, 10]
# Explanation: The bottom-most element will be 10 and the top-most element will be 40.
# Middle element will be element at index 2 from bottom, which is 20. Deleting 20, stack will look like {10 30 40}.

# Input: s = [5, 8, 6, 7, 6, 6, 5, 10, 12, 9]
# Output: [9, 12, 10, 5, 6, 7, 6, 8, 5]

# Constraints:
# 2 ≤ element of stack ≤ 10^5
# 2 ≤ s.size() ≤ 10^4

# Optimal
# T.C. - O(N^2)
# S.C  - O(N) [recursion stack space]

# Intuition
# Assume that the a function takes a stack s as input and the mid pos (k) to delete
# and it delets the mid element of the stack (hypothesis), Now try thinking for
# smaller input run the same function for k-1, now we can say after the mid element
# has been removed we are left to append the popped element at the back (Induction).
# The base case can be thought of as what if we have k==1 only when we are at the
# middle element


class Solution:
    def deleteMid(self, stack: list[int]) -> list[int]:
        def solve(stack: list[int], k: int) -> list[int]:
            # Base
            if k == 1:
                stack.pop(-1)
                return stack

            # Hypo
            topElement = stack.pop(-1)
            stack = solve(stack, k - 1)

            # Induction
            stack.append(topElement)
            return stack

        return solve(stack, (len(stack) // 2) + 1)[::-1]
