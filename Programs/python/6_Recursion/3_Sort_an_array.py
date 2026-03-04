# https://leetcode.com/problems/sort-an-array, Medium, IBH

# Question
# Given an array of integers nums, sort the array in ascending order and return it.

# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

# Example 1:

# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
# Example 2:

# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessarily unique.


# Constraints:

# 1 <= nums.length <= 5 * 10^4
# -5 * 10^4 <= nums[i] <= 5 * 10^4


# Brute
# T.C. - O(n^2)
# S.C  - O(n)

# Intuition
# Use the IBH method for sorting recursion
# H -> define sortArray will sort the array given nums as the array to sort
# B -> if n is less than equal to 1 just return arr
# I -> we using Hypothesis sort the array from 1 to n-1 and then for the nth element
# we try to find its best insertion point using upper bound
# Use the IBH method for finding correct place of insertion of num in a sorted array
# H -> define insertElemToCorrectPlace will insert a given num n to a sorted_arr
# B -> if length of sorted_arr is equal to zero return the num
# I -> we using Hypothesis insert the given num n to the sorted_arr from 0 to n-1,
# and atlast insert the largest element at last as induction


from typing import List


class Solution:
    def insertElemToCorrectPlace(self, sorted_arr: list[int], num: int):
        # Base
        if len(sorted_arr) == 0 or sorted_arr[-1] <= num:
            sorted_arr.append(num)
            return

        # Hypothesis
        largest_elem = sorted_arr.pop(-1)
        self.insertElemToCorrectPlace(sorted_arr, num)

        # Induction
        sorted_arr.append(largest_elem)

    def sortArray(self, nums: List[int]) -> List[int]:
        # Base
        if len(nums) <= 1:
            return nums

        # Hypothesis
        last_val = nums.pop(-1)
        self.sortArray(nums)

        # Induction
        self.insertElemToCorrectPlace(nums, last_val)

        return nums


# Brute
# T.C. - O(n^2)
# S.C  - O(n)

# Intuition
# Use the IBH method for recursion
# H -> define sortArray will sort the array given nums as the array to sort
# B -> if n is less than equal to 1 just return arr
# I -> we using Hypothesis sort the array from 1 to n-1 and then for the nth element
# we try to find its best insertion point using upper bound


from typing import List
from bisect import bisect_right


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Base
        if len(nums) <= 1:
            return nums

        # Hypothesis
        last_val = nums.pop(-1)
        self.sortArray(nums)

        # Induction
        best_idx = bisect_right(nums, last_val)
        nums.insert(best_idx, last_val)

        return nums
