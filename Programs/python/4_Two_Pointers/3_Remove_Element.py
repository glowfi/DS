# https://leetcode.com/problems/remove-element, Easy, Two Pointers

# Question
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed.
# Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The
# remaining elements of nums are not important as well as the size of nums.
# Return k.
# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int val = ...; // Value to remove
# int[] expectedNums = [...]; // The expected answer with correct length.
#                             // It is sorted with no values equaling val.

# int k = removeElement(nums, val); // Calls your implementation

# assert k == expectedNums.length;
# sort(nums, 0, k); // Sort the first k elements of nums
# for (int i = 0; i < actualLength; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.

# Example 1:
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2:
# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Constraints:
# 0 <= nums.length <= 100
# 0 <= nums[i] <= 50
# 0 <= val <= 100

# Brute
# T.C. - O(n)
# S.C  - O(n)

# Intuition
# store all the non zero values in a temporary array
# assign nums to temporary array
# return the length of nums array

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ls = []

        for i in nums:
            if i != val:
                ls.append(i)
        nums[:] = ls[:]

        return len(ls)


# Optimal
# T.C. - O(n)
# S.C  - O(1)

# Intuition
# All elements that are not equal to val should end up on the left side of the array,
# and all occurrences of val can be pushed to the right (their positions don’t matter after removal).
# We only care about how many non-val elements remain and that they occupy the first k positions.
# To do this, think of one pointer k as the position where the next “kept” element (not equal to val) should go,
# and another pointer idx that scans through the array. As we scan:
# If nums[idx] is not val, we swap it into position k and move k forward.
# If nums[idx] is val, we just skip it.


from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        idx = 0

        while idx < len(nums):
            if nums[idx] != val:
                nums[idx], nums[k] = nums[k], nums[idx]
                k += 1
            idx += 1

        return k
