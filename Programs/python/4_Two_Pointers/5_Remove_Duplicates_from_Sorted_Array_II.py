# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii, Medium, Two Pointers

# Question
# Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place
# such that each unique element appears at most twice. The relative order of the elements should be kept the same.
# Since it is impossible to change the length of the array in some languages, you must instead
# have the result be placed in the first part of the array nums. More formally, if there are k
# elements after removing the duplicates, then the first k elements of nums should hold the final result.
# It does not matter what you leave beyond the first k elements.
# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

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
# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2:
# Input: nums = [0,0,1,1,1,1,2,3,3]
# Output: 7, nums = [0,0,1,1,2,3,3,_,_]
# Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).


# Constraints:
# 1 <= nums.length <= 3 * 10^4
# -10^4 <= nums[i] <= 10^4
# nums is sorted in non-decreasing order.

# Brute
# T.C. - O(n)
# S.C  - O(n)

# Intuition
# We use two pointers , k to keep track of the position
# to insert unique element and i to traverse the whole
# array, if we see an element that we have not seen before
# or if the element is visited but its visted count is less than 2,
# we add it to the kth index and mark it as visited

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        visited = {}
        k = 0

        for i in range(len(nums)):
            if nums[i] not in visited or (visited.get(nums[i], 0)) < 2:
                nums[k] = nums[i]
                k += 1

            visited[nums[i]] = 1 + visited.get(nums[i], 0)

        return k


# Optimal
# T.C. - O(n)
# S.C  - O(1)

# Intuition
# The array is sorted, so equal elements are grouped together. We want each
# element to appear at most twice in the final array.
#
# We use:
# - i      : to traverse the array from left to right (starting at index 1)
# - k      : to mark the position where the next allowed element should be placed
# - count  : to track how many times the current value has appeared consecutively
#
# The logic follows two simple rules:
# 1) If we see the *same* element as the previous one:
#      - If count < 2, we are allowed to keep it, so we write it at index k
#        and increase both k and count.
#      - If count == 2, we skip it (do nothing), because we already kept two.
#
# 2) If we see a *new* element (different from the previous one):
#      - We reset count to 1 (first occurrence of this new value),
#        write it at index k, and move k forward.


from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        count = 1

        for i in range(1, len(nums)):
            if count < 2 and nums[i] == nums[i - 1]:
                nums[k] = nums[i]
                k += 1
                count += 1

            elif nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                count = 1
                k += 1

        return k
