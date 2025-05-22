# https://leetcode.com/problems/sort-colors , Medium

# Question
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.


# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]


# Constraints:

# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.


# Brute
# T.C. - O(Nlog(N))
# S.C  - O(1)

# Intuition
# sort using inbilt function


from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()


# Better
# T.C. - O(N)+O(3*N) ~ O(N)
# S.C  - O(3)

# Intuition
# Count occurences of 0s,1s,2s and store them in a map
# Then fill the array with the number of times each element occurs


from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count_map = {0: 0, 1: 0, 2: 0}

        for num in nums:
            count_map[num] += 1

        idx = 0
        for num, count in count_map.items():
            for i in range(count):
                nums[idx] = num
                idx += 1


# Optimal
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# Use dutch national flag algorithm
# goal of this algo is to push all the low values to left
# and high values to right
# at first our entire array is unsorted
# so we can put the mid at 0 and high at len(array)-1
# and start in the 0 th postiion

# 00000000000000     111111111111     ?????????         2222222222
# ^            ^     ^          ^     ^       ^         ^        ^
# 0         low-1   low     mid-1    mid      high     high+1   n-1

# ? is ith unsorted portion


from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, mid = 0, 0
        high = len(nums) - 1

        for _ in range(len(nums)):
            # if unsorted portion has zero
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            # if unsorted portion has one
            elif nums[mid] == 1:
                mid += 1

            # if unsorted portion has two
            elif nums[mid] == 2:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
