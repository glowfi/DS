# https://www.geeksforgeeks.org/problems/delete-middle-element-of-a-stack/1, Easy, IBH

# Question
# Given a stack s, delete the middle element of the stack without using any additional data structure.

# Middle element:- floor((size_of_stack+1)/2) (1-based indexing) from the bottom of the stack.

# Note: The output shown by the compiler is the stack from top to bottom.

# Examples:

# Input: s = [10, 20, 30, 40, 50]
# Output: [50, 40, 20, 10]
# Explanation: The bottom-most element will be 10 and the top-most element will
# be 50. Middle element will be element at index 3 from bottom, which is 30. Deleting 30, stack will look like {10 20 40 50}.

# Input: s = [10, 20, 30, 40]
# Output: [40, 30, 10]
# Explanation: The bottom-most element will be 10 and the top-most element will be 40.
# Middle element will be element at index 2 from bottom, which is 20. Deleting 20, stack will look like {10 30 40}.

# Input: s = [5, 8, 6, 7, 6, 6, 5, 10, 12, 9]
# Output: [9, 12, 10, 5, 6, 7, 6, 8, 5]
# Constraints:
# 2 ≤ element of stack ≤ 10^5
# 2 ≤ s.size() ≤ 10^4

# Brute
# T.C. - O(n)
# S.C  - O(n)

# Intuition
# Use the IBH method
# H -> define delete_k method which given a stack deletes the kth element from top
# B -> if k==1 then delete the top element
# I -> we using Hypothesis we make our input smaller by taking only 0 to n-1 and since
# we eliminate one element our k becomes k-1 and we delete the k-1 th element now,at last
# we append the eliminated element


from typing import List


class Solution:
    def deleteMid(self, stack: List[int]) -> List[int]:
        def delete_k(stack: List[int], k: int) -> List[int]:
            # Base
            if k == 1:
                stack.pop(-1)
                return stack

            # Hypothesis
            last_elem = stack.pop(-1)
            delete_k(stack, k - 1)

            # Induction
            stack.append(last_elem)
            return stack

        k = len(stack) // 2 + 1
        return delete_k(stack, k)
