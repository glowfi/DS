# https://leetcode.com/problems/missing-number , Easy, CyclicSort

# Question
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Example 1:

# Input: nums = [3,0,1]

# Output: 2

# Explanation:

# n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

# Example 2:

# Input: nums = [0,1]

# Output: 2

# Explanation:

# n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

# Example 3:

# Input: nums = [9,6,4,2,3,5,7,0,1]

# Output: 8

# Explanation:

# n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.


# Constraints:

# n == nums.length
# 1 <= n <= 10^4
# 0 <= nums[i] <= n
# All the numbers of nums are unique.


# Optimal
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# Since numbers are in range of 1 to n
# first find sum of natural numbers from 1 to n
# and substract the current sum of the array , we
# will get the missing number


from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        actualSum = n * (n + 1) // 2
        currSum = sum(nums)
        return actualSum - currSum


# Optimal
# T.C. - O(2N) ~ O(N)
# S.C  - O(1)

# Intuition
# use cyclic sort


from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0

        while i < len(nums):
            actualPos = nums[i]
            if nums[i] < len(nums) and nums[actualPos] != nums[i]:
                nums[i], nums[actualPos] = nums[actualPos], nums[i]
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] != i:
                return i

        return len(nums)
