# https://leetcode.com/problems/find-all-duplicates-in-an-array , Medium, CyclicSort

# Question
# Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer
# appears at most twice, return an array of all the integers that appears twice.

# You must write an algorithm that runs in O(n) time and uses only constant auxiliary space, excluding the space needed to store the output


# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]
# Example 2:

# Input: nums = [1,1,2]
# Output: [1]
# Example 3:

# Input: nums = [1]
# Output: []


# Constraints:

# n == nums.length
# 1 <= n <= 10^5
# 1 <= nums[i] <= n
# Each element in nums appears once or twice.

# Brute
# T.C. - O(2N) ~ O(N)
# S.C  - O(N)

# Intuition
# use map to keep track of frequency
# number occuring more than 2 are duplicates


from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq_mp = {}

        for num in nums:
            freq_mp[num] = 1 + freq_mp.get(num, 0)

        ans = []
        for num in freq_mp:
            if freq_mp[num] >= 2:
                ans.append(num)

        return ans


# Optimal
# T.C. - O(2N) ~ O(N)
# S.C  - O(1)

# Intuition
# do cyclic sort
# numbers not at its correct place are the duplicates


from typing import List


class Solution:
    def cyclic_sort(self, nums: List[int]) -> None:
        i = 0
        while i < len(nums):
            actualPos = nums[i] - 1
            if nums[actualPos] != nums[i]:
                nums[i], nums[actualPos] = nums[actualPos], nums[i]
            else:
                i += 1

    def findDuplicates(self, nums: List[int]) -> List[int]:
        self.cyclic_sort(nums)
        ans = []

        for i in range(len(nums)):
            if nums[i] != i + 1:
                ans.append(nums[i])

        return ans
