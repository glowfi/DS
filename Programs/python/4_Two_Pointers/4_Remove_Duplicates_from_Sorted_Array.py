# https://leetcode.com/problems/remove-duplicates-from-sorted-array, Easy, Two Pointers

# Question
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same.
# Consider the number of unique elements in nums to be k. After removing duplicates, return the number of unique elements k.

# The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.

# Custom Judge:
# The judge will test your solution with the following code:
# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length
# int k = removeDuplicates(nums); // Calls your implementation
# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.


# Example 1:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2:
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Constraints:
# 1 <= nums.length <= 3 * 10^4
# -100 <= nums[i] <= 100
# nums is sorted in non-decreasing order.

# Brute
# T.C. - O(n)
# S.C  - O(n)

# Intuition
# We use two pointers , k to keep track of the position
# to insert unique element and i to traverse the whole
# array, if we see an element that we have not seen before,
# we add it to the kth index and mark it as visited

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        visited = {}
        k = 0

        for i in range(len(nums)):
            if nums[i] not in visited:
                nums[k] = nums[i]
                k += 1
            visited[nums[i]] = 1

        return k


# Optimal
# T.C. - O(n)
# S.C  - O(1)

# Intuition
# Since array is sorted we are going to take use this property to our advantage
# we take two pointers k and i , k stores the index to put the unique element to
# and i traverse the array.The moment we see the last element does not match our
# current element we are sure that we are seeing this first time and we can move
# this element to the kth index and also move the kth index by one after placing
# the current element

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k
