# https://www.geeksforgeeks.org/problems/find-pairs-with-given-sum-in-doubly-linked-list/1 , Easy, 2Pointers

# Question
# Given a sorted doubly linked list of positive distinct elements, the task is to find pairs in a doubly-linked list whose sum is equal to given value target.


# Example 1:

# Input:
# 1 <-> 2 <-> 4 <-> 5 <-> 6 <-> 8 <-> 9
# target = 7
# Output: (1, 6), (2,5)
# Explanation: We can see that there are two pairs
# (1, 6) and (2,5) with sum 7.


# Example 2:

# Input:
# 1 <-> 5 <-> 6
# target = 6
# Output: (1,5)
# Explanation: We can see that there is one pairs  (1, 5) with sum 6.


# Your Task:
# You don't need to read input or print anything. Your task is to complete the function findPairsWithGivenSum() which takes head node of the doubly linked list and an integer target as input parameter and returns an array of pairs. If there is no such pair return empty array.

# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(1)
# Constraints:
# 1 <= N <= 10^5
# 1 <= target <= 10^5


# Optimal
# T.C. - O(N)+O(N)
# S.C  - O(1)

# Intuition
# Find tail
# use 2 pointer approach to find pairs
# if we are far from target increase range
# if we are overshooting decrease range


from typing import Optional
from typing import List


class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
        self.prev = None


class Solution:
    def findPairsWithGivenSum(
        self, target: int, head: Optional["Node"]
    ) -> List[List[int]]:
        end = head

        while end.next:
            end = end.next

        start = head
        ans = []

        while start.data < end.data:
            if start.data + end.data > target:
                end = end.prev
            elif start.data + end.data < target:
                start = start.next
            else:
                ans.append([start.data, end.data])
                start = start.next
                end = end.prev

        return ans
