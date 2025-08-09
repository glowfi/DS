# https://leetcode.com/problems/remove-duplicates-from-sorted-array , Easy, Basic

# Question
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.
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
# T.C. - O(N)+O(Klog(K))+O(K)
# S.C  - O(K)

# Intuition
# store the unique nums to a set datastructure
# fill the first k position of the array with elements
# in the datastructure


from typing_extensions import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        visited_nums = set()
        for i in range(len(nums)):
            visited_nums.add(nums[i])

        for idx, val in enumerate(
            sorted(visited_nums)
        ):  # since sets do not maintain order we need to sort again
            nums[idx] = val

        return len(visited_nums)


# Optimal
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# keep track of k which is the last element inserted position
# we also declare a last num which keeps track of the last number visited
# if we visit a new number we update last visited num and insert the number
# at k position and atlast return k

from typing_extensions import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        last_visted_num = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != last_visted_num:
                last_visted_num = nums[i]
                nums[k] = nums[i]
                k += 1
            else:
                last_visted_num = nums[i]
        return k
